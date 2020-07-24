from selenium.webdriver.common.by import By
import time
from driver.browser import chrome_driver


class ContractCase():
    def __init__(self,driver):
        self.driver = driver

        #元素定位符
        self.dw_into_contract = (By.LINK_TEXT,'合同')        #进入合同
        self.dw_add_contract = (By.CSS_SELECTOR, 'a[class="btn btn-primary"]>i') #点击添加合同
        self.dw_contract = (By.ID, 'business_name')                    #点击来源商机
        self.dw_contract_xz = (By.XPATH, '//tbody[@id="data"]/tr[3]/td[1]/input[1]')  #选择商机
        self.dw_contract_dj = (By.CSS_SELECTOR, 'div[id="dialog-business"]+div span:nth-child(1)')  #点击ok
        self.dw_preservation = (By.NAME, 'submit')          #保存
        self.dw_duanyan = (By.CLASS_NAME,'alert.alert-success')

    def ele_into_contract(self):
        self.driver.find_element(*self.dw_into_contract).click()

    def ele_add_contract(self):
        self.driver.find_element(*self.dw_add_contract).click()


    def ele_contract(self):
        self.driver.find_element(*self.dw_contract).click()  # 点击来源商机
        self.driver.find_element(*self.dw_contract_xz).click()  # 选择商机
        self.driver.find_element(*self.dw_contract_dj).click()  # ok

    def ele_preservation(self):
        self.driver.find_element(*self.dw_preservation).click()  # 保存

    def add_preservation(self):
        self.ele_into_contract()
        self.ele_add_contract()
        self.ele_contract()
        self.ele_preservation()
        time.sleep(2)
        shiji = self.driver.find_element(*self.dw_duanyan).text
        self.driver.quit()
        return shiji

# c = ContractCase()
# c.add_preservation()