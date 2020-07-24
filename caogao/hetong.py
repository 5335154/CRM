from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_case.test_alogin import LoginTestCase

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
url = "http://192.168.1.120/index.php?m=user&a=login"
driver.get(url=url)

#登录
driver.find_element(By.NAME, 'name').clear()
driver.find_element(By.NAME, 'name').send_keys("admin")
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys("banxian123")
driver.find_element(By.NAME, 'submit').click()

#进入合同页面
driver.find_element(By.LINK_TEXT,'合同').click()
#添加合同
driver.find_element(By.CSS_SELECTOR,'a[class="btn btn-primary"]>i').click()

driver.find_element(By.ID,'business_name').click()                                         #点击来源商机
driver.find_element(By.XPATH,'//tbody[@id="data"]/tr[3]/td[1]/input[1]').click()           #选择商机
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-business"]+div span:nth-child(1)').click() #ok
driver.find_element(By.NAME,'submit').click()        #保存


time.sleep(3)
driver.quit()