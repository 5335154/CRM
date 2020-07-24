import time
from selenium.webdriver.common.by import By
from driver.browser import chrome_driver
from page.base_page import BasePage

class LoginCase(BasePage):
    def __init__(self):
        super().__init__()
        self.url = "http://192.168.1.120/index.php?m=user&a=login"
        #元素定位符

    def ele_search(self):
        self.driver.find_element(By.LINK_TEXT,'财务').click()

    def ele_finance(self):
        pass



