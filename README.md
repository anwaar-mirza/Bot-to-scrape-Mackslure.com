# Bot-to-scrape-Mackslure.com
mackslure.com is an ecommerce website that sells Fishing instruments.

## Overview

This Python script automates the scraping of product data from the Mackslure website. It extracts product details such as titles, prices, variants, sizes, descriptions, and image URLs, and stores the data in CSV format for further analysis.

## Features

- **Dynamic Web Scraping:** Utilizes `selenium` to interact with the website and dynamically fetch data.
- **Product Categories:** Supports multiple product categories including Trout Lures, Walleye Lures, Kokanee Lures, and more.
- **Multi-Threading:** Executes scraping tasks in parallel using Python's threading module.
- **Data Export:** Saves scraped data in CSV format with a timestamped filename.
- **Randomized User-Agent:** Uses `fake_useragent` to minimize detection during web scraping.

## Prerequisites

Before running the script, ensure the following dependencies are installed:

- Python 3.7+
- Selenium
- Webdriver Manager
- Fake UserAgent
- Pandas

Install all dependencies using:

```bash
pip install selenium webdriver-manager fake-useragent pandas
```

## Script Usage

### Class: `MackslaureData`

This class handles the core scraping functionality, including browser setup, navigation, and data extraction.

#### Methods

1. **`__init__()`**:
   - Sets up the Selenium WebDriver with randomized User-Agent and incognito mode.

2. **`select_product_to_scrape(product_to_scrape)`**:
   - Navigates to a specific product category based on the input.

3. **`get_product_links()`**:
   - Collects links to all product listings in the selected category.

4. **`land_targeted_page(page_url)`**:
   - Opens a specific product page.

5. **`get_listing_title()`**:
   - Retrieves the title of the current product.

6. **`get_price()`**:
   - Fetches the price of the product.

7. **`get_varients()`**:
   - Extracts available variants of the product.

8. **`get_size()`**:
   - Extracts available sizes of the product.

9. **`get_description()`**:
   - Retrieves the product description.

10. **`get_images()`**:
   - Collects URLs of product images.

11. **`current_url()`**:
   - Returns the current page URL.

### Function: `choice_to_scrape(choice)`

Maps user input to predefined product categories.

### Function: `execution_process(ch)`

Coordinates the scraping process:
- Navigates to the selected category.
- Extracts product data.
- Writes the data to a CSV file.

### Multi-Threading

The script launches multiple threads (`th1` to `th7`) to scrape different product categories concurrently.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/anwaar-mirza/Bot-to-scrape-Mackslure.com
```

2. Run the script:

```bash
python Mackslaure.py
```

3. The script will create a `data` directory in the current working directory and store the results as timestamped CSV files.

## Directory Structure

```plaintext
|-- Mackslaure.py
|-- data/
    |-- <category>-<timestamp>.csv
```

## Output Format

The data is saved as CSV with the following columns:

- Title
- Price
- Varients
- Size
- Description
- Images
- Listing URL
- Listing URL

## Notes

- Make sure the `chromedriver` executable is compatible with your installed Chrome browser version.
- The script dynamically adjusts zoom to handle webpage elements effectively.
- Error handling is in place for failed attempts to scrape data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Conclusion

This script provides an efficient and automated way to scrape product information from the Macks Lure website. Its features, including multi-threading and dynamic data extraction, make it a powerful tool for anyone needing organized and detailed product data for analysis or research purposes. With its robust design and ease of use, this scraper simplifies the task of collecting extensive product details from an online catalog. Contributions and improvements to the script are always welcome to expand its capabilities further.
