# Flipkart Scraping Program 
## Overview
This Python script is designed to scrape product information from Flipkart based on a user-defined search query. It extracts product titles, prices, and links from the search results and saves this information into a CSV file. The script uses Selenium to automate the browser for data extraction and BeautifulSoup to parse the HTML.

## Modules Required
To run this script successfully, you need to install the following Python modules:

`selenium`: For web automation and interaction.
`beautifulsoup4`: For parsing HTML and extracting data.
`pandas`: For handling data and saving it into a CSV file.
`html`: Built-in library for handling HTML entities (usually not needed explicitly).
`re`: Built-in library for regular expressions (usually not needed explicitly).

## Installation Guide
Follow these steps to set up the environment and run the script:

1. Install Python:
Make sure you have Python 3.x installed on your system. You can download it from python.org.

2. Install Required Modules:
You can install the required modules using pip. Open your command line or terminal and run the following commands:

```bash
pip install selenium beautifulsoup4 pandas
```
If you're using a virtual environment, ensure it's activated before running these commands.

3. Download WebDriver:
The script uses the Chrome WebDriver. Download it from `ChromeDriver` and ensure it's in your system's PATH. For convenience, you can place the chromedriver executable in the same directory as your script.

4. Save and Run the Script:
Save the script to a file, e.g., `flipkart_scraper.py`. Open your terminal or command prompt, navigate to the directory where the script is saved, and run:

```bash
python flipkart_scraper.py
```
5. Enter Search Query:
When prompted, enter the search query for which you want to scrape product information.

### Script Details
* Initialization: Opens the Flipkart search page based on the user input.
* Pagination Handling: Determines the total number of pages to scrape.
* Data Extraction: Collects HTML content for each product, parses it to extract titles, prices, and links.
* Data Storage: Saves the extracted data to a CSV file named based on the search query.
### Example

```python
query = input("Search for...")
```
The user inputs a search query. For instance, entering "laptop" will scrape all the pages of search results for laptops.

```python
print(f"Total pages: {pages}")
```
Displays the total number of pages to be scraped.

```python
df.to_csv(f'data/{query}.csv')
```
Saves the scraped data into a CSV file named according to the search query.

### Troubleshooting
***Module Not Found Error***: Ensure all required modules are installed.\
***WebDriver Issues***: Ensure chromedriver is correctly installed and in your system's PATH.\
***HTML Parsing Issues***: Verify that the class names used for finding elements are up-to-date with the current Flipkart page structure.\
For further assistance, you can refer to the `Selenium documentation` and `BeautifulSoup documentation`.# Web-Scraping
