import time

from selenium.webdriver.common.by import By


class SwichToClient():
    def __init__(self, driver):
        self.driver = driver
        # 元素定位符
        self.dw_click_clue = (By.LINK_TEXT, '线索')  # 点击线索
        self.dw_clicl_switch = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[2]')  # 点击转换
        self.dw_click_sava = (By.NAME, 'submit')  # 保存
        self.dw_duanyan = (By.CLASS_NAME, 'alert.alert-success')  # 断言

    def ele_click_clue(self):
        self.driver.find_element(*self.dw_click_clue).click()  # 点击线索

    def ele_clicl_switch(self):
        self.driver.find_element(*self.dw_clicl_switch).click()  # 点击转换

    def ele_click_sava(self):
        self.driver.find_element(*self.dw_click_sava).click()  # 保存

    def switchclient(self):
        '''转换客户'''
        self.ele_click_clue()
        self.ele_clicl_switch()
        self.ele_click_sava()
        time.sleep(2)
        jieguo = self.driver.find_element(*self.dw_duanyan).text
        time.sleep(1)
        return jieguo

# sc = SwichToClient()
# sc.switchclient()
