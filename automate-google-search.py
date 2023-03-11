"""
USAGE - This script opens a specified number of browser windows (in this case, one), and in each window, it opens the Google homepage, 
        enters the search term into the search box, and submits the search. The code uses the ChromeDriverManager package to 
        manage the installation of the Chrome WebDriver, and it sets some options for the Chrome browser instance, such as keeping 
        the window open after the script finishes running.
        
AUTHOR - https://github.com/Ahendrix9624/
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SEARCH_TERM = "Selenium"
NUM_BROWSERS = 1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

for _ in range(NUM_BROWSERS):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.google.com/")
    search = driver.find_element(By.NAME, "q")
    search.send_keys(SEARCH_TERM)
    search.submit()
