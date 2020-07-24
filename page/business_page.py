import time
from selenium.webdriver.common.by import By
from driver.browser import chrome_driver
from page.base_page import BasePage
from page.login_page import LoginCase
from test_case.test_alogin import LoginTestCase

class BusinessCase(BasePage):
    def __init__(self,driver):
        # super().__init__()
        self.driver = driver
        # self.url = "http://192.168.1.120/index.php?m=user&a=login"
        # self.driver.get(url=self.url)

        #元素定位符
        self.dw_into_bus = (By.LINK_TEXT,'商机')          #进入商机页面
        self.dw_add_bus = (By.CSS_SELECTOR,'div[class="pull-right"]>a')  #添加商机
        self.dw_bus_name = (By.ID,'name')                #商机名
        self.dw_yprice = (By.ID, 'estimate_price')       #预计成交价
        self.dw_customer = (By.ID, 'customer_name')                                               #点击选择客户
        self.dw_customer_xz = (By.XPATH, '//tbody[@id="datas"]/tr[4]/td[1]/input[1]')             #选择客户
        self.dw_customer_ok = (By.CSS_SELECTOR, 'div[id="dialog-message"]+div>div :nth-child(1)') #点击ok
        self.dw_responsible = (By.ID, 'owner_name')                                                     #点击选择负责人
        self.dw_responsible_xz = (By.XPATH, '//tbody[@id="d_content"]/tr[1]/td[1]/input')               #选择负责人
        self.dw_responsible_ok = (By.CSS_SELECTOR, 'div[id="dialog-role-list"]+div>div :nth-child(1)')  #点击ok
        self.dw_product = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[12]/th/input')                    #点击添加产品
        self.dw_product_xz = (By.XPATH, '//tbody[@id="data"]/tr[1]/td[1]/input[1]')                        #选择产品
        self.dw_product_ok = (By.CSS_SELECTOR, 'div[id="dialog-product-list"]+div>div :nth-child(1)')      #点击ok
        self.dw_preservation = (By.XPATH, '//form[@id="form1"]/table/tfoot/tr/td/input[1]')     #保存
        self.dw_duanyan = (By.CLASS_NAME, 'alert.alert-success')                         #断言

    def ele_into_bus(self):
        self.driver.find_element(*self.dw_into_bus).click()

    def ele_add_bus(self):
        self.driver.find_element(*self.dw_add_bus).click()

    def ele_bus_name(self,bus_name):
        self.driver.find_element(*self.dw_bus_name).send_keys(bus_name)

    def ele_yprice(self,yprice):
        self.driver.find_element(*self.dw_yprice).send_keys(yprice)

    def ele_customer(self):
        self.driver.find_element(*self.dw_customer).click()  # 选择客户
        self.driver.find_element(*self.dw_customer_xz).click()
        self.driver.find_element(*self.dw_customer_ok).click()

    def ele_responsible(self):
        self.driver.find_element(*self.dw_responsible).click()  # 选择负责人
        self.driver.find_element(*self.dw_responsible_xz).click()
        self.driver.find_element(*self.dw_responsible_ok).click()  # 点击OK

    def ele_add_product(self):
        self.driver.find_element(*self.dw_product).click()  # 添加产品
        self.driver.find_element(*self.dw_product_xz).click()
        self.driver.find_element(*self.dw_product_ok).click()  # 点击OK

    def ele_preservation(self):
        self.driver.find_element(*self.dw_preservation).click()  # 点击保存

    def add_bus_opp(self,bus_name,yprice):
        self.ele_into_bus()
        self.ele_add_bus()
        self.ele_bus_name(bus_name)
        self.ele_yprice(yprice)
        self.ele_customer()
        self.ele_responsible()
        self.ele_add_product()
        self.ele_preservation()
        time.sleep(2)
        shiji = self.driver.find_element(*self.dw_duanyan).text
        time.sleep(1)
#        self.quit()
        return shiji

# bus = BusinessCase()
# bus.add_bus_opp("王辉商机4号","13322")