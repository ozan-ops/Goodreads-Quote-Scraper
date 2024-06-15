# Goodreads Quote Scraper

The Goodreads Quote Scraper is a Python script that extracts quotes from the Goodreads website using web scraping techniques. It gathers quotes from multiple pages, cleans them by removing unnecessary characters, and provides a set of unique quotes as output.

## Usage

1. Clone the repository or download the `Goodreads Quote Scraper.py` file.
2. Make sure you have Python installed on your system.
3. Install the required libraries using pip:

    ```
    pip install requests bs4
    ```

4. Run the script using Python:

    ```
    python Goodreads Quote Scraper.py
    ```

5. The script will start scraping quotes from Goodreads and display the unique set of quotes collected.

## Requirements

- Python 3.x
- requests
- BeautifulSoup (bs4)

## How It Works

The script sends HTTP requests to Goodreads, parses the HTML content of each page using BeautifulSoup, and extracts quotes from the page. It then cleans the quotes by removing newline characters and other unnecessary characters. Finally, it provides a set of unique quotes collected from the specified pages on Goodreads.
