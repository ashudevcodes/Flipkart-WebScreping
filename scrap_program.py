# Import necessary libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Initialize empty lists to store data
reviews = []
names = []
prices = []
links = []

# Loop through 30 pages of a Flipkart search for "keyboard skin"
for a in range(1, 31):
    # Create the URL for each page
    url = f"https://www.flipkart.com/search?q=keyboard+skin&sid=6bo%2Cai3&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_6_0_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_6_0_na_na_na&as-pos=6&as-type=HISTORY&suggestionId=keyboard+skin|Laptop+Accessories&requestId=aa75ee24-a7c4-4783-a4cb-a0d7f95c0823&page={a}"
    
    # Define user-agent headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
    
    # Send an HTTP GET request to the URL
    r = requests.get(url, headers=headers)
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(r.text, "lxml")
    
    # Find all product containers on the page
    products = soup.find_all("div", class_="_4ddWXP")

    # Extract and store product reviews
    for i in products:
        allpr = i.find_all("span", class_="_2_R_DZ")
        if allpr == []:
            allpr = (BeautifulSoup(
                '''<span class="_2_R_DZ">(0)</span>''', 'html.parser'))
        for j in allpr:
            reviews.append(j.text)

    # Extract and store product names
    for l in products:
        name = l.find_all("a", class_="s1Q9rs")
        if name == []:
            name = (BeautifulSoup('''<a class="s1Q9rs" href="/saco-chiclet-keyboard-skin-dell-inspiron-15-3558-15-6-inch-core-i3-5005u-4gb-1tb-windows-10-integrated-graphics-black-pre-loaded-ms-office-2016-home-student/p/itmeqsgbgjts5faf?pid=KSNEQSGBF2GMKPJW&amp;lid=LSTKSNEQSGBF2GMKPJWHEB1J9&amp;marketplace=FLIPKART&amp;q=keyboard+skin&amp;store=6bo%2Fai3&amp;srno=s_2_80&amp;otracker=AS_QueryStore_HistoryAutoSuggest_6_0_na_na_na&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_6_0_na_na_na&amp;fm=organic&amp;iid=3ac5f04d-4490-45a6-94f3-d1faa8e0b696.KSNEQSGBF2GMKPJW.SEARCH&amp;ppt=None&amp;ppn=None&amp;ssid=ja9qssvceo0000001693752624380&amp;qH=e75f17a89f161240" rel="noopener noreferrer" target="_blank" title="Saco Chiclet Keyboard Skin for Dell Inspiron 15 3558 15.6-inch (Core i3-5005U/4GB/1TB/Windows 10/Integrated Graphics), Black With Pre-Loaded MS Office 2016 Home &amp; Student edition Keyboard Skin">No Name</a>''', 'html.parser'))
        for k in name:
            names.append(k.get('title'))

    # Extract and store product prices
    for m in products:
        money = m.find_all("div", class_="_30jeq3")
        if money == []:
            money = (BeautifulSoup(
                '''<div class="_30jeq3">Free</div>''', 'html.parser'))
        for p in money:
            prices.append(p.text)

    # Extract and store product links
    for o in products:
        c = o.find_all("a", class_="s1Q9rs")
        for q in c:
            links.append("https://www.flipkart.com" + q.get('href'))

# Create a DataFrame to organize the collected data
df = pd.DataFrame(list(zip(reviews, names, prices, links)),
                  columns=['review', 'name', 'price', 'link'])

# Clean and preprocess the data
df['price'] = df['price'].str.replace('₹', '').str.replace(',', '').astype(int)
df['name'] = df['name'].str.lower()

# Filter products containing "cover" or "skin" in their names
ks = df[df['name'].str.contains('cover', regex=True) | (
    df['name'].str.contains('skin', regex=True))]

# Reset the DataFrame index and drop the old index column
ks = ks.reset_index()
ks = ks.drop(columns=["index"])

# Print the filtered DataFrame
print(ks)

# Save the filtered data to a CSV file named "scrap_data"
ks.to_csv("scrap_data")
