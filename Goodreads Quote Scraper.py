import requests
import bs4

# Base URL for fetching quotes
base_link = "https://www.goodreads.com/quotes?page={}"

# List to store quotes
quotes = []

# Loop through pages 1 to 10 to scrape quotes
for i in range(1, 11):
    new_url = base_link.format(i)  # Generate the URL for the current page
    res = requests.get(new_url)  # Send a GET request to the URL
    soup = bs4.BeautifulSoup(res.text, 'lxml')  # Parse the HTML content of the page

    len_quotes = len(soup.select(".quoteText"))  # Count the number of quotes on the page

    # Iterate through each quote on the page and extract the text
    for n in range(len_quotes):
        quote = soup.select(".quoteText")[n].getText().strip()  # Extract the text of the quote
        quotes.append(quote)  # Add the quote to the list

# Clean the quotes by removing newline characters
cleaned_quotes = [quote.replace('\n', '') for quote in quotes]

# Print the unique set of cleaned quotes
print(set(cleaned_quotes))
