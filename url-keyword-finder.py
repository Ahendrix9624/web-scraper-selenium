"""
USAGE - This code scrapes an article from a given URL and looks for instances of a specified keyword within the article. 
    It uses Selenium and BeautifulSoup libraries to scrape the article, and writes the results to a file. 
    The user is prompted to enter the URL and keyword, and the script outputs the number of matches found for the keyword 
    and the name of the file where the results are stored. The code also includes a function to clear the terminal screen and 
    checks for existing filenames to avoid overwriting existing files.
        
AUTHOR - https://github.com/Ahendrix9624/
"""
import os
import re
import codecs

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def clear_screen():
    """
    Clears the terminal screen regardless of windows/linux/mac
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_article_matches(page_source, keyword):
    soup = BeautifulSoup(page_source, features="html.parser")
    matches = soup.body.find_all(string=re.compile(keyword))
    len_match = len(matches)
    title = soup.title.text
    return matches, len_match, title


def write_article_to_file(title, matches, len_match, filename):
    with codecs.open(filename, "a+") as file:
        file.write(title + "\n")
        file.write("The following are all instances of your keyword:\n")
        count = 1
        for i in matches:
            file.write(f"{count}. {i}\n")
            count += 1
        file.write(f"There were {len_match} matches found for the keyword.\n")


def main():
    clear_screen()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    val = input("Enter a url: ")
    wait = WebDriverWait(driver, 10)
    driver.get(val)

    get_url = driver.current_url
    wait.until(EC.url_to_be(val))

    if get_url == val:
        page_source = driver.page_source

    clear_screen()
    keyword = input("Enter a keyword to find instances of in the article: ")
    matches, len_match, title = get_article_matches(page_source, keyword)

    filename = "article_scraping.txt"
    count = 1
    while os.path.exists(filename):
        count += 1
        filename = f"article_scraping_{count}.txt"

    write_article_to_file(title, matches, len_match, filename)

    print(f"There were {len_match} matches found for the keyword.")
    print(f"Check your current directory for {filename}")

    driver.quit()


if __name__ == '__main__':
    main()

