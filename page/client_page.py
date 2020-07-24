import time

from selenium.webdriver.common.by import By

from driver.browser import chrome_driver
from page.login_page import LoginCase


class Client():
    '''添加客户'''
    def __init__(self, driver):
        self.driver = driver
        self.locator1 = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a')
        self.locator2 = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]')
        self.locator3 = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/a')
        self.locator4 = (By.NAME, 'name')
        self.locator5 = (By.ID, 'ownership1')
        self.locator6 = (By.NAME, 'submit')
        self.locator7 = (By.ID, 'owner_name')
        self.locator8 = (By.XPATH, '//tbody[@id="d_content"]/tr[2]/td[1]/input')
        self.locator9 = (By.XPATH,'/html/body/div[7]/div[3]/div/button[1]/span')
        self.locator10 = (By.ID, 'share')
        self.locator11 = (By.XPATH,'/html/body/div[5]/div[2]')
    def click_client(self):    #点击客户
        self.driver.find_element(*self.locator1).click()
    def click_cat(self):       #点击查看
        self.driver.find_element(*self.locator2).click()
    def click_new(self):       #点击新建客户
        self.driver.find_element(*self.locator3).click()
    def send_name(self,name):  #客户名称输入名字
        self.driver.find_element(*self.locator4).send_keys(name)
    def company(self):         #选择公司性质
        self.driver.find_element(*self.locator5).click()
    def click_save(self):      #点击保存
        self.driver.find_element(*self.locator6).click()
    def click_owner(self):     #点击负责人
        self.driver.find_element(*self.locator7).click()
    def select_owner(self):    #选择负责人
        self.driver.find_element(*self.locator8).click()
        self.driver.find_element(*self.locator9).click()
    def reslut_catc(self):     #获取查看断言的文本信息
        res = self.driver.find_element(*self.locator10).text
        return res
    def reslut_ac(self):       #获取添加用户断言信息
        res1 = self.driver.find_element(*self.locator11).text
        return res1
    def cat_client(self):      #获取添加用户不放入客户池的断言信息
        '''查看客户信息'''
        self.click_client()
        self.click_cat()
        res = self.reslut_catc()
        return res
        time.sleep(2)
    def add_client(self, name):
        '''添加客户放入客户池'''
        self.click_client()
        self.click_new()
        self.send_name(name)
        self.company()
        time.sleep(2)
        self.click_save()
        res1 = self.reslut_ac()
        return res1

    def add_client2(self, name):
        '''添加客户并不放入客户池'''
        self.click_client()
        self.click_new()
        self.send_name(name)
        self.click_owner()
        self.select_owner()
        self.company()
        self.click_save()
        res2 = self.reslut_ac()
        return res2
class Client1():
    def __init__(self,driver):
        self.driver = driver
        self.locator1 =(By.LINK_TEXT, '编辑')
        self.locator2 = (By.NAME, 'name')
        self.locator3 = (By.NAME, 'submit')
        self.locator4 = (By.XPATH, '/html/body/div[5]/div[2]')
        self.locator5 = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a')
    def click_client(self):    #点击客户
        self.driver.find_element(*self.locator5).click()
    def click_vim(self):            #点击编辑客户
        self.driver.find_element(*self.locator1).click()
    def send_newname(self,newname):  #清除文本并将输入新信息
        self.driver.find_element(*self.locator2).clear()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(*self.locator2).send_keys(newname)
    def clicl_savavim(self):         #点击保存
        self.driver.find_element(*self.locator3).click()
    def assert_vim(self):            #获取断言信息
        res4 = self.driver.find_element(*self.locator4).text
        return res4
    def vim_client(self,newman):
        self.click_client()
        self.click_vim()
        self.send_newname(newman)
        self.clicl_savavim()
        res4 = self.assert_vim()
        return res4



# driver =chrome_driver()
# b = LoginCase(driver)
# b.login('admin', 'banxian123')
# a = Client1(driver)
# c = a.vim_client('xiaohuwei3')
# print(c)



