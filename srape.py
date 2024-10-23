import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching chrome browser...")

    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(Service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Pae loaded...")
        html = driver.page_source
        time.sleep()

        return html
    finally:
        driver.quit()