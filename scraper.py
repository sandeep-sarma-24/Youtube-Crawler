from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrape_data(limit, proxies_to_use, search_query):
    # Create a DataFrame to store the scraped data
    df = pd.DataFrame(columns=['link', 'title', 'channel'])

    # Define a list of proxies to use with Selenium
    proxy_list = [
        # ... Your proxies list ...
        "34.95.214.235:3129",
        "34.125.211.252:8080",
        "183.239.62.59:9091",
        "34.87.84.105:80",
        "128.140.9.127:8080",
        "58.246.58.150:9002",
        "195.181.172.213:8081",
        "198.44.161.71:45787",
        "47.253.214.60:9999",
        "190.52.178.17:80",
        "35.247.229.47:3129",
        "195.181.152.71:3128",
        "65.109.168.231:8080",
        "137.184.100.135:80",
        "222.138.76.6:9002",
        "121.37.203.216:1081",
        "120.236.79.139:9002",
        "82.180.163.163:80",
        "223.85.12.114:2222",
        "34.76.73.21:80",
        "65.21.61.55:80",
        "34.95.187.154:3129",
        "104.225.220.233:80",
        "109.254.67.104:9090"
        # Add more proxies here...
    ]

    # Use only the required number of proxies
    proxy_list = proxy_list[:proxies_to_use]

    # URL for YouTube search
    base_url = "https://www.youtube.com/results?search_query="

    # Loop through each proxy in the list
    for proxy_address in proxy_list:
        # Set up the proxy
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpsProxy': 'https://' + proxy_address,
        })

        # Set up the Chrome driver with the selected proxy
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server=%s' % proxy.http_proxy)
        options.add_argument('--proxy-server=%s' % proxy.http_proxy)
        #options.add_argument('--headless') # This line enables headless mode
        driver = webdriver.Chrome(options=options)

        try:
            # Go to the target URL
            driver.get(base_url + search_query)

            # ... The rest of your script ...
            wait = WebDriverWait(driver, 10)
            # Initialize a count to keep track of the number of videos scraped
            count = 0

            # Keep scrolling and scraping until the limit is reached
            while count < limit:
                # Find all the video elements on the page
                video_elements = driver.find_elements(
                    By.CSS_SELECTOR, "ytd-video-renderer")

                # Loop through each video element and extract the link, title, and channel
                for video_element in video_elements:
                    # Extract the video link
                    v_link = video_element.find_element(By.CSS_SELECTOR, "a.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail").get_attribute('href')
                
                    # Extract the video title
                    v_title = video_element.find_element(
                        By.CSS_SELECTOR, "#video-title").text
                    # Extract the channel link
                    c_link = video_element.find_element(
                        By.CSS_SELECTOR, "ytd-channel-name a").get_attribute('href')

                    # Add the scraped data to the DataFrame if the link is not already in it
                    if v_link not in df['link'].values:
                        df.loc[len(df)] = [v_link, v_title, c_link]

                    # Increment the count
                    count += 1
                    # If the limit is reached, break the loop
                    if count >= limit:
                        break

                # Scroll down to load more videos
                driver.execute_script(
                    "window.scrollTo(0, document.documentElement.scrollHeight);")
                # Wait for new videos to load
                time.sleep(1)

            # Print a success message
            print(f"Successful to connect to proxy server: {proxy_address}")
            driver.quit()
            
        except Exception as e:
            print(f"Failed to connect to proxy server: {proxy_address}")
            print(f"Error message: {str(e)}")
            driver.quit()
            continue
        # Convert dataframe to list of dictionaries
    return df.to_dict('records')
