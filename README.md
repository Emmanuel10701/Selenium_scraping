# E-commerce Reviews Scraping

This Python project scrapes customer reviews from an e-commerce website (or a local HTML file) and saves the extracted data into both **CSV** and **Excel** formats. It uses libraries like **Selenium**, **Pandas**, and **openpyxl** to achieve this.

## Features
- Scrapes reviews, including customer ratings, comments, and review dates.
- Saves the scraped data in both **CSV** and **Excel** formats.
- Automates browser interactions to dynamically load pages for scraping.
- Option to scrape multiple pages of reviews.
- Visualizes the ratings of reviews in an area plot.
- Added the collab file in jupyter format to classify grades of students.

## Requirements

Before using this project, ensure that **Python** is installed on your machine, and the necessary libraries are set up.

### 1. Python Installation:
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - After installation, verify by running the following command in your terminal:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
     This should print the Python version (e.g., `Python 3.x.x`).

### 2. Library Installation:
   The following Python libraries are required to run this project:
   - **selenium**: For browser automation and dynamically interacting with web pages.
   - **pandas**: For handling and saving the scraped data.
   - **openpyxl**: For saving data to an Excel file.
   - **numpy**: For data handling and numeric operations.
   - **matplotlib**: For visualizing the ratings in an area plot.
   - **webdriver-manager**: For managing the WebDriver for Selenium.

   To install the required libraries, open your terminal and run the following command:
   ```bash
   pip install -r requirements.txt
