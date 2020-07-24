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

#点击搜索
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(2)').click() #统计
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(1)').click() #商机
driver.find_element(By.LINK_TEXT,'我负责的').click()
driver.find_element(By.LINK_TEXT,'下属创建的').click()
driver.find_element(By.LINK_TEXT,'今日需联系').click()
driver.find_element(By.LINK_TEXT,'30日未联系').click()
driver.find_element(By.LINK_TEXT,'最近更新').click()
driver.find_element(By.LINK_TEXT,'本月需联系').click()
driver.find_element(By.LINK_TEXT,'7日未联系').click()
driver.find_element(By.LINK_TEXT,'回收站').click()
#选择条件搜索
ele = driver.find_element(By.ID,'field')
select = Select(ele)
select.select_by_index(3)

ele = driver.find_element(By.ID,'condition')
select = Select(ele)
select.select_by_index(0)
driver.find_element(By.ID,"search").send_keys("大商机")
driver.find_element(By.ID,'dosearch').click()


time.sleep(2)
driver.quit()