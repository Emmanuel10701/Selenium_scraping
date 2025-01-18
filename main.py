from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

# Function to scrape reviews from a URL using Selenium
def scrape_reviews_with_selenium(target_url):
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no browser UI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    service = Service("path/to/chromedriver")  # Replace with the path to your ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)

    reviews = []

    try:
        # Open the target URL
        driver.get(target_url)

        # Wait for the content to load (optional, you can use explicit waits for specific elements)
        driver.implicitly_wait(10)

        # Extract review elements
        review_elements = driver.find_elements(By.CLASS_NAME, "review")
        for element in review_elements:
            try:
                username = element.find_element(By.CLASS_NAME, "username").text.strip()
                rating = element.find_element(By.CLASS_NAME, "rating").text.strip()
                comment = element.find_element(By.CLASS_NAME, "comment").text.strip()
                reviews.append({
                    "Username": username,
                    "Rating": rating,
                    "Comment": comment
                })
            except Exception as e:
                print(f"Error extracting review: {e}")
                continue
    finally:
        # Close the WebDriver
        driver.quit()

    return reviews

# Target URL
TARGET_URL = "https://www.sitejabber.com/reviews/jumia.com"

# Scrape the reviews
reviews_data = scrape_reviews_with_selenium(TARGET_URL)

# Save data to CSV and Excel
if reviews_data:
    # Convert to a DataFrame
    df = pd.DataFrame(reviews_data)

    # Save to CSV
    csv_file = "customer_reviews.csv"
    df.to_csv(csv_file, index=False, encoding="utf-8")
    print(f"Reviews have been saved to {csv_file}")

    # Save to Excel
    excel_file = "customer_reviews.xlsx"
    df.to_excel(excel_file, index=False, engine="openpyxl")  # Use 'openpyxl' for Excel files
    print(f"Reviews have been saved to {excel_file}")
else:
    print("No reviews found.")
