# Ecommerce Scraping Tool

A Python-based web scraper that extracts product details such as titles, prices, and links from eCommerce websites like Amazon. This project uses **Selenium WebDriver** for automating browser interaction and **BeautifulSoup** for parsing the HTML to extract the desired data. The results are saved in a CSV file for easy analysis.

## Features:
- Scrapes product **titles**, **prices**, and **links** from eCommerce product pages.
- Uses **Selenium** to handle dynamic page rendering and interactions.
- Automates navigation across **multiple pages** of search results.
- **Logs** the scraping process to track progress and errors.
- Saves the scraped product data to a **CSV file**.

## Technologies Used:
- **Python 3.x** (Ensure you use Python 3.7 or later)
- **Selenium WebDriver**: For browser automation.
- **BeautifulSoup**: For parsing HTML and extracting product data.
- **pandas**: For storing and saving the scraped data to CSV.
- **chromedriver**: Required for running Selenium with Chrome browser.

## Installation & Setup:

### 1. Clone the Repository:
```bash
git clone https://github.com/Akhil-215/ecommerce-scraping-tool.git
2. Set Up a Virtual Environment (Recommended):
Creating a virtual environment helps manage dependencies for this project without affecting other Python projects you might have.

On Windows:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate
On macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies:
Install the required libraries by running:

bash
Copy code
pip install -r requirements.txt
This will install the necessary libraries like Selenium, BeautifulSoup4, pandas, etc.

4. Download ChromeDriver:
The scraper uses Selenium WebDriver with ChromeDriver to interact with the Amazon pages. Download ChromeDriver from the following link and make sure it's compatible with your installed version of Google Chrome:

Download ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

Once downloaded, ensure that chromedriver is accessible from your system's PATH or place it in the project folder and update the path in your script if necessary.

5. Run the Scraper:
To start the scraper, run the following command:

bash
Copy code
python main.py
The script will begin scraping eCommerce product pages (e.g., Amazon) and store the extracted data in a CSV file called amazon_products.csv in the same directory.

Note:
Ethical Use: Please use this scraper responsibly and ensure you're adhering to Amazon's Terms of Service.

This scraper is intended for educational purposes only. Use it for learning or personal use only. Scraping large volumes of data from websites like Amazon may violate their policies, so please be mindful of usage limits and frequency to avoid IP blocking.

Future Improvements:
Extend the scraper to collect more product details such as reviews, ratings, and availability.

Add error handling to manage unexpected page structures or missing elements.

Implement periodic scraping and store data over time to track price changes.

Add more flexibility to scrape different product categories or regions (e.g., amazon.co.uk, amazon.de).

License:
This project is licensed under the MIT License. See the LICENSE file for more details.

markdown
Copy code

---

### Key Changes:
1. **Updated Repository Link**: Changed the clone URL to `https://github.com/Akhil-215/ecommerce-scraping-tool.git` in the **Clone the Repository** section.
2. **Updated Project Title**: Changed the title from `Amazon Product Scraper` to `Ecommerce Scraping Tool` to reflect the new repository name.
3. **Corrected the Description**: The project now uses the term "eCommerce" to make it more generic, as you're not scraping only Amazon anymore. You can easily extend it to scrape other platforms as well.

### Next Steps:
1. **Update Your Repository**: If this README file is now ready, commit and push it to your GitHub repository.
   ```bash
   git add README.md
   git commit -m "Update README with new repository name and clone URL"
   git push