import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import sys

args = sys.argv[1:]

if len(args) > 1:
    searchFor = args[0]
    titleClassName = args[1]
    priceClassName = args[2]
    reviewClassName = args[3]
    prodctLinkClassName = args[4]
    print(titleClassName, priceClassName, reviewClassName, prodctLinkClassName)
else:
    searchFor = input("tell me what are you searching for ? ")

    titleClassName = input(
        '''
    Find the class name of title and past here
    Title ClassName: '''
    )

    priceClassName = input(
        '''
    Find the class name of price and past here
    Price ClassName: '''
    )

    reviewClassName = input(
        '''
    Find span tag with contains rating class name and past here
    Rating ClassName: '''
    )

    prodctLinkClassName = input(
        '''
    Find a tag with contains link of products and past here
    Products ClassName: '''
    )


# fileHandle = open("./temp.html")


def scrapeTitleData(htmlData, className):
    '''Storing the title data in names Array if given className was avelable.

    Args:
         param1 (str): HTML file in a formet of `lxml`
         param2 (str): classname which was use to specify atag class

    '''
    soup = BeautifulSoup(htmlData, "lxml")
    products = soup.find_all(class_=className)

    try:
        _ = products[0]
    except Exception:
        print("No Title data avelable")
        return

    for domeNode in products:
        names.append(domeNode.get_text())


def scrapePriceData(htmlData, className):
    '''this function use for storing prices of all the products.

    Args:
         param1 (str): HTML file in a formet of `lxml`
         param2 (str): classname which was use to specify prices div className

    '''
    soup = BeautifulSoup(htmlData, "lxml")
    products = soup.find_all("div", class_=className)

    try:
        _ = products[0]
    except Exception:
        print("No Price data avelable")
        return

    for divTags in products:
        prices.append(divTags.get_text())


def scrapeReviewsData(htmlData, className):
    '''this function is use for storing review count of a specific products
        in reviews Array.

    Args:
         param1 (str): HTML file in a formet of `lxml`
         param2 (str): classname which was use to specify span class

    '''
    soup = BeautifulSoup(htmlData, "lxml")
    products = soup.find_all(
        "span", class_=className)

    try:
        _ = products[0]
    except Exception:
        print("No Reviews data avelable")
        return

    for spanTags in products:
        reviews.append(spanTags.find("span").find("span").get_text(strip=True))


def scrapeProductlinks(htmlData, className):
    '''function is use for storing products links in links Array.

    Args:
         param1 (str): HTML file in a formet of `lxml`
         param2 (str): classname which was use to specify atag class

    '''
    soup = BeautifulSoup(htmlData, "lxml")
    products = soup.find_all(
        "a", class_=className, href=True)

    try:
        _ = products[0]
    except Exception:
        print("No Link data avelable")
        return

    for spanTags in products:
        links.append(f"https://www.flipkart.com{spanTags['href']}")


reviews = []
names = []
prices = []
links = []

# scrapeTitleData(fileHandle, titleClassName)
# scrapePriceData(fileHandle, priceClassName)
# scrapeReviewsData(fileHandle, reviewClassName)
# scrapeProductlinks(fileHandle, prodctLinkClassName)


for pageNumber in range(1, 2):
    url = f"https://www.flipkart.com/search?q={searchFor}&page={pageNumber}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }
    res = requests.get(url, headers=headers)
    scrapeTitleData(res.text, titleClassName)
    scrapePriceData(res.text, priceClassName)
    scrapeReviewsData(res.text, reviewClassName)
    scrapeProductlinks(res.text, prodctLinkClassName)


# Create a DataFrame to organize the collected data

if not reviews:
    df = pd.DataFrame(list(zip(names, prices, links)),
                      columns=['name', 'price', 'link'])
else:
    df = pd.DataFrame(list(zip(names, prices, reviews, links)),
                      columns=['name', 'price', 'reviews', 'link'])


print(df)

df.to_csv("allProducts.csv")
