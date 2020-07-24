import time
from selenium.webdriver.common.by import By
from driver.browser import chrome_driver


class ClueCase():
    def __init__(self,driver):
        self.driver = driver
        #元素定位符
        self.dw_click_clue = (By.LINK_TEXT,'线索')                            #点击线索
        self.dw_click_new_clue = (By.CSS_SELECTOR,'div[class="pull-right"]>a') #新建线索
        self.dw_send_name = (By.ID, 'name')                                  #公司名
        self.dw_send_pname = (By.ID, 'contacts_name')                       #联系人姓名
        self.dw_click_save = (By.NAME, 'submit')                            #保存
        self.dw_duanyan = (By.CLASS_NAME,'alert.alert-success')            #断言

    def ele_click_clue(self):
        self.driver.find_element(*self.dw_click_clue).click()     #点击线索

    def ele_click_new_clue(self):
        self.driver.find_element(*self.dw_click_new_clue).click()  #新建线索

    def ele_send_name(self,name):
        self.driver.find_element(*self.dw_send_name).send_keys(name)    #公司名

    def ele_send_pname(self,pname):
        self.driver.find_element(*self.dw_send_pname).send_keys(pname)   #联系人姓名

    def ele_click_save(self):
        self.driver.find_element(*self.dw_click_save).click()     #保存

    def add_clue(self,name,pname):
        '''新增线索'''
        self.ele_click_clue()
        self.ele_click_new_clue()
        self.ele_send_name(name)
        self.ele_send_pname(pname)
        self.ele_click_save()
        time.sleep(2)
        jieguo = self.driver.find_element(*self.dw_duanyan).text
        time.sleep(1)
        return jieguo

# b =ClueCase()
# b.add_clue('xhw','dengdeng')
