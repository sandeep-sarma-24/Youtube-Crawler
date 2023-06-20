# Scraper Website

This is a web application built with Flask that allows you to scrape YouTube videos based on a search query. It utilizes Selenium for web scraping and supports the use of proxies for data collection. The scraped video data is displayed in a user-friendly format.

## Features

- Input the search query, limit, and number of proxies to use.
- Scrape YouTube videos based on the provided search query.
- Display the scraped video data, including the title, video link, and channel link.
- Supports the use of proxies for data collection.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python 3.x
- Flask
- Selenium
- Pandas
- Chrome browser
- ChromeDriver

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/scraper-website.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the proxies list and other configurations in the `scraper.py` file.

4. Run the Flask application:

   ```bash
   flask run
   ```

5. Open your web browser and navigate to `http://localhost:5000` to access the scraper website.

## Usage

1. Enter the search query, limit, and number of proxies to use in the input fields.
2. Click on the "Start Scraping" button to initiate the scraping process.
3. Wait for the scraping to complete. The progress and status will be displayed.
4. Once the scraping is finished, the scraped video data will be displayed in a tabular format.
5. Use the provided links to watch the videos or visit the respective YouTube channels.

