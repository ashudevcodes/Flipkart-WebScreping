# Flipkart Web Scraping utilty
<kdb><img width="1919" height="1079" src="https://github.com/user-attachments/assets/62f96743-b73c-4890-8e8e-d6d9445ae080" /></kdb>

A program to scrape product information from [Flipkart](https://www.flipkart.com) search result pages. The script extracts product titles, prices, reviews, and links, then saves the data into a CSV file for easy analysis.

## Features

- **Command-line and Interactive Modes**:  
  - Pass all required class names and search query as command-line arguments, or
  - Run interactively and enter details when prompted.
- **Customizable Scraping**:  
  Specify the class names for product titles, prices, reviews, and product links for better adaptability to Flipkart's frequently changing HTML structure.
- **CSV Output**:  
  Results are saved in `allProducts.csv` for convenient analysis.

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (For fast and isolated package management)
- pip (for initial setup if not using `uv`)

## Installation

1. **Install [uv](https://github.com/astral-sh/uv):**
   ```bash
   pip install uv
   ```
   or follow instructions on the [uv GitHub page](https://github.com/astral-sh/uv#installation).

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

## Usage

### 1. Command-line Mode

You can run the script by passing all required parameters:
```bash
uv run main.py "<search_query>" "<title_class>" "<price_class>" "<review_class>" "<product_link_class>"
```
Example:
```bash
uv run main.py "mobile" "4rR01T" "30jeq3" "LWZlK" "fQZEK"
```

### 2. Interactive Mode

If you run the script without command-line arguments, it will prompt you to input:
- The search query (what you want to search for)
- The class names for title, price, reviews, and product link

```bash
uv run main.py
```
Then, follow the prompts.

### 3. Output

- After the script runs, it will print the scraped data as a table.
- It will save the results in a file named `allProducts.csv` in the current directory.

## Finding Class Names

1. Go to [Flipkart](https://www.flipkart.com) and search for your desired product.
2. Use your browser's developer tools (F12) to inspect the HTML elements for product titles, prices, reviews, and product links.
3. Copy their class names and use them as script arguments or input.

## Notes

- The script scrapes only the first page of results by default. You can modify the `range` in the script to scrape multiple pages.
- Flipkart's HTML structure may change over time, so you may need to update the class names regularly.

## Disclaimer

This script is for educational purposes only.  
Scraping websites may violate their Terms of Service. Use responsibly.
