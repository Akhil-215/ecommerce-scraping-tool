import os
import random
import time
import logging
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of User-Agents (this should be much larger in production, you can load it from a file)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    # Add many more here
]

# Randomly select a user agent to rotate
user_agent = random.choice(user_agents)

# Set up Chrome options
options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_argument("Accept-Language: en-US,en;q=0.9")
#options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (not necessary in headless)
options.add_argument("--no-sandbox")  # For Docker environments

# Specify path for chromedriver if needed (Ensure it's on your PATH or specify it explicitly)
driver = webdriver.Chrome(options=options)

# Define the URL structure and results dictionary
query = "Laptop"
final_result = {
    "Title": [],
    "Price": [],
    "Link": []
}


# Function to fetch data from a given Amazon page
def fetch_page_data(page_num):
    """Fetch data from a specific page on Amazon."""
    try:
        url = f"https://www.amazon.in/s?k={quote_plus(query)}&page={page_num}"  # URL encoding
        driver.get(url)

        # Wait for the page to load completely (wait for the search result container)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "puis-card-container")))

        # Find all product containers on the page
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        logging.info(f"Found {len(elems)} items on page {page_num}.")

        return elems
    except TimeoutException:
        logging.error(f"TimeoutException on page {page_num}. Retrying...")
        return None
    except WebDriverException as e:
        logging.error(f"WebDriverException on page {page_num}: {str(e)}")
        return None


# Function to parse individual product data
def parse_product_data(elems):
    """Parse and extract title, price, and link from product element."""
    for elem in elems:
        try:
            soup = BeautifulSoup(elem.get_attribute('outerHTML'), "html.parser")

            # Extracting the title, link, and price from the soup object
            title_elem = soup.find("h2")
            title = title_elem.get_text() if title_elem else "No title available"

            link_elem = soup.find("a", class_="a-link-normal")
            link = "https://www.amazon.in" + link_elem["href"] if link_elem else "No link available"

            price_elem = soup.find("span", class_="a-price-whole")
            price = price_elem.get_text() if price_elem else "No price available"

            # Validate price data
            if price != "No price available" and price != "No title available":
                try:
                    # Ensure price is numeric
                    price = float(price.replace(",", "").replace("₹", "").strip())
                except ValueError:
                    price = "Invalid price"

            # Append to the final results if data is valid
            if title != "No title available" and price != "Invalid price" and price != "No price available":
                final_result["Title"].append(title)
                final_result["Price"].append(price)
                final_result["Link"].append(link)
            else:
                logging.warning(f"Skipping product with missing or invalid data: {title}")

        except Exception as e:
            logging.error(f"Error parsing product data: {str(e)}")
            continue  # Continue parsing next product even if one fails


# Scraping process
def scrape_amazon():
    """Scrape data from multiple pages on Amazon."""
    for page_num in range(1, 11):  # Scrape first 10 pages
        logging.info(f"Scraping page {page_num}...")
        elems = fetch_page_data(page_num)

        if elems:
            parse_product_data(elems)

        # Random sleep between pages to avoid hitting Amazon too fast
        time.sleep(random.uniform(2, 5))

    logging.info(f"Scraping completed. {len(final_result['Title'])} products found.")

    # Save the results to a CSV file
    try:
        df = pd.DataFrame(final_result)
        df.to_csv("amazon_products.csv", index=False)
        logging.info("Data saved to amazon_products.csv")
    except Exception as e:
        logging.error(f"Error saving data to CSV: {str(e)}")


# Ensure driver quits properly even if there’s an error
try:
    scrape_amazon()
finally:
    driver.quit()  # Always close the browser
