from selenium.webdriver.common.by import By
from driver.browser import chrome_driver


class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def duanyan(self):
        shiji = self.driver.current_url
        return shiji

    def open(self,url):
        self.driver.get(url=url)

    def quit(self):
        self.driver.quit()


