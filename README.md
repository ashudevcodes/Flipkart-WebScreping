# Flipkart Keyboard Skin Scraper

This Python program is a web scraper that extracts information about keyboard skins available on Flipkart. It collects data such as product reviews, names, prices, and links, and then filters the products that contain the keywords "cover" or "skin" in their names. The filtered data is saved to a CSV file named "scrap_data." You can also scrape data on Flipkart by changing the class of tags in the program. Feel free to make modifications as needed. 

## Requirements

Before using this program, make sure you have the following requirements installed:

- Python 3.x
- Required Python libraries: requests, pandas, BeautifulSoup (bs4)

You can install the required libraries using pip:

```bash
pip install requests pandas beautifulsoup4
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the folder where you've saved the program files.

3. Run the program by executing the following command:

   ```bash
   python flipkart_scraper.py
   ```

   This will start the web scraping process. The program will fetch data from Flipkart's search results pages for "keyboard skin."

4. Once the scraping is complete, the program will generate a DataFrame with the collected data and filter products containing "cover" or "skin" in their names.

5. The filtered data will be displayed on the terminal, and it will also be saved to a CSV file named "scrap_data.csv" in the same directory.

## Customization

You can customize the program by modifying the following variables in the code:

- `url`: You can change the Flipkart search URL to target different search results.

- `headers`: You can modify the user-agent in the headers to mimic different web browsers.

- Keywords for filtering: If you want to filter products based on different keywords, you can adjust the `df['name'].str.contains('cover', regex=True)` and `df['name'].str.contains('skin', regex=True)` conditions in the code.

## Data Output

The program generates a CSV file named "scrap_data.csv" containing the following columns:

- `review`: Product reviews.
- `name`: Product names (lowercased).
- `price`: Product prices (in INR).
- `link`: Product links on Flipkart.

## Disclaimer

This program is for educational purposes and should be used responsibly and in compliance with Flipkart's terms of service and scraping policies. Be mindful of rate limiting and avoid overloading Flipkart's servers.
