# import selenium.webdriver as webdriver
# from selenium.webdriver.chrome.service import Service
# import time


# def scrape_website(website):
#     print("Launching chrome browser...")

#     chrome_driver_path = "chromedriver.exe"
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

#     try:
#         driver.get(website)
#         print("Pae loaded...")
#         html = driver.page_source
#         time.sleep(10)

#         return html
#     finally:
#         driver.quit()

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")


def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


