from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_case.test_alogin import LoginTestCase

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
url = "http://localhost/index.php?m=user&a=login"
driver.get(url=url)

#登录
driver.find_element(By.NAME, 'name').clear()
driver.find_element(By.NAME, 'name').send_keys("admin")
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys("banxian123")
driver.find_element(By.NAME, 'submit').click()

#进入商机页面
driver.find_element(By.LINK_TEXT,'商机').click()

#添加商机
driver.find_element(By.CSS_SELECTOR,'div[class="pull-right"]>a').click()    #添加商机

driver.find_element(By.ID,'name').send_keys("地球2号商机")        #商机名
driver.find_element(By.ID,'estimate_price').send_keys("10000")  #预计成交价
driver.find_element(By.ID,'customer_name').click()  #选择客户
driver.find_element(By.XPATH,'//tbody[@id="datas"]/tr[4]/td[1]/input[1]').click()
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message"]+div>div :nth-child(1)').click()  #点击OK
driver.find_element(By.ID,'owner_name').click()    #选择负责人
driver.find_element(By.XPATH,'//tbody[@id="d_content"]/tr[1]/td[1]/input').click()
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-role-list"]+div>div :nth-child(1)').click()  #点击OK
driver.find_element(By.XPATH,'//form[@id="form1"]/table/tbody/tr[12]/th/input').click()  #添加产品
driver.find_element(By.XPATH,'//tbody[@id="data"]/tr[1]/td[1]/input[1]').click()
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-product-list"]+div>div :nth-child(1)').click()  #点击OK
driver.find_element(By.XPATH,'//form[@id="form1"]/table/tfoot/tr/td/input[1]').click() #点击保存

time.sleep(2)
driver.quit()