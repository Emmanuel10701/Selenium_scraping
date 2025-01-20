import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

        # Example scraping logic
        reviews = []
        ratings = []
        review_elements = driver.find_elements(By.CLASS_NAME, "review")  # Adjust the selector as needed
        rating_elements = driver.find_elements(By.CLASS_NAME, "rating")  # Adjust the selector as needed

        for review, rating in zip(review_elements, rating_elements):
            reviews.append(review.text)
            
            # Attempt to clean the rating string and convert it to a float
            rating_text = rating.text.strip()
            try:
                # If the rating is in the format "5/5", we can extract the first number
                if "/" in rating_text:
                    rating_value = float(rating_text.split("/")[0])
                else:
                    rating_value = float(rating_text)
                ratings.append(rating_value)
            except ValueError:
                ratings.append(np.nan)  # If conversion fails, append NaN

        # Return as DataFrame
        return pd.DataFrame({"Review": reviews, "Rating": ratings})

    except Exception as e:
        print(f"Error: {e}")
        return None  # Return None in case of error
    finally:
        # Ensure the driver quits even if an error occurs
        driver.quit()

# Save to CSV and Excel
def save_to_files(df, csv_path, excel_path):
    df.to_csv(csv_path, index=False)
    df.to_excel(excel_path, index=False)

# Visualize Data
def visualize_data(df, img_path):
    plt.figure(figsize=(10, 6))
    plt.barh(df["Review"].str[:30], df["Rating"], color="skyblue")
    plt.xlabel("Rating")
    plt.ylabel("Review (Truncated)")
    plt.title("Ratings of Reviews")
    plt.tight_layout()
    plt.savefig(img_path)
    plt.show()

# Main script
if __name__ == "__main__":
    # Specify the target file
    TARGET_FILE = "file2.html"
    TARGET_URL = f"file://{os.path.abspath(TARGET_FILE)}"

    # Scrape the reviews
    df_reviews = scrape_reviews_with_selenium(TARGET_URL)

    if df_reviews is not None and not df_reviews.empty:
        # File paths
        CSV_PATH = "reviews.csv"
        EXCEL_PATH = "reviews.xlsx"
        IMAGE_PATH = "ratings_plot.png"

        # Save data to CSV and Excel
        save_to_files(df_reviews, CSV_PATH, EXCEL_PATH)

        # Visualize the data
        visualize_data(df_reviews, IMAGE_PATH)

        print(f"Data saved to:\nCSV: {CSV_PATH}\nExcel: {EXCEL_PATH}\nImage: {IMAGE_PATH}")
    else:
        print("No reviews were found.")
