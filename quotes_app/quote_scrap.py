import time
from selenium import webdriver

def trial(url):
    driver = webdriver.Chrome()
    driver.get(url)
    pageSource = driver.page_source

    driver.quit()
    return pageSource