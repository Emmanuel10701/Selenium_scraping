from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# Function to scrape reviews
def scrape_reviews_with_selenium(target_url):
    # Configure ChromeDriver options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open the target URL
        driver.get(target_url)

        # Example scraping logic (modify as per your requirement)
        reviews = []
        review_elements = driver.find_elements(By.CLASS_NAME, "review")  # Adjust the selector as needed

        for review in review_elements:
            reviews.append(review.text)

        return reviews

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the driver quits even if an error occurs
        driver.quit()

# Main script
if __name__ == "__main__":
    # Specify the target file
    TARGET_FILE = "file2.html"

    # Convert the file path to a fully qualified URL
    TARGET_URL = f"file://{os.path.abspath(TARGET_FILE)}"

    # Scrape the reviews
    reviews_data = scrape_reviews_with_selenium(TARGET_URL)

    # Output the scraped reviews
    print("Scraped Reviews:")
    for review in reviews_data:
        print(review)
