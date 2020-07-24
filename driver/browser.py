'''浏览器驱动'''
from selenium import webdriver

def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver
