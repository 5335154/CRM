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
#进入财务页面
driver.find_element(By.LINK_TEXT,'财务').click()
#点击搜索
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(2)').click() #应付款
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(3)').click() #应收款
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(4)').click() #收款单
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(5)').click() #付款单
driver.find_element(By.CSS_SELECTOR,'ul[class="nav nav-tabs"] :nth-child(1)').click() #统计
driver.find_element(By.LINK_TEXT,'我负责的').click()
driver.find_element(By.LINK_TEXT,'下属创建').click()
driver.find_element(By.LINK_TEXT,'未收款').click()
driver.find_element(By.LINK_TEXT,'已收款').click()
driver.find_element(By.LINK_TEXT,'今日应收').click()
driver.find_element(By.LINK_TEXT,'本月应收').click()
driver.find_element(By.LINK_TEXT,'最近修改').click()
driver.find_element(By.LINK_TEXT,'回收站').click()
#选择条件搜索
ele = driver.find_element(By.ID,'field')
select = Select(ele)
select.select_by_index(1)
ele = driver.find_element(By.ID,'condition')
select.select_by_index(1)
driver.find_element(By.ID,"search").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,'li[class="pull-left"] button').click()

#添加应收款——保存
driver.find_element(By.CSS_SELECTOR,'div[class="pull-right"]>a').click()

driver.find_element(By.NAME,'name').send_keys("李逍遥")        #应收款名
driver.find_element(By.ID,'contract_name').click()               #点击合同
driver.find_element(By.XPATH,'//tbody[@id="data"]/tr[2]/td[1]/input').click()    #选择合同
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message2"]+div>div :nth-child(1)').click()   #点击OK

driver.find_element(By.ID,'customer').click()      #点击客户
driver.find_element(By.XPATH,'//tbody[@id="datas"]/tr[3]/td[1]/input[1]').click()   #选择客户
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message"]+div>div :nth-child(1)').click()  #点击OK

driver.find_element(By.ID,'owner_name').click()     #点击负责人
driver.find_element(By.XPATH,'//tbody[@id="d_content"]/tr[3]/td[1]/input').click()  #选择负责人
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message3"]+div>div :nth-child(1)').click()  #点击OK

driver.find_element(By.ID,'price').clear()     #清空收款金额框
driver.find_element(By.ID,'price').send_keys("10000") #输入收款金额

driver.find_element(By.ID,'pay_time').send_keys("2020-07-23")  #输入日期
driver.find_element(By.XPATH,'//textarea[@class="span6" and @name="description"]').send_keys("123321") #输入描述

driver.find_element(By.XPATH,'//input[@value="保存"]').click()   #点击保存
time.sleep(2)

#添加应收款——保存并新建
driver.find_element(By.CSS_SELECTOR,'div[class="pull-right"]>a').click()

driver.find_element(By.NAME,'name').send_keys("李逍遥")        #应收款名
driver.find_element(By.ID,'contract_name').click()               #点击合同
driver.find_element(By.XPATH,'//tbody[@id="data"]/tr[2]/td[1]/input').click()    #选择合同
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message2"]+div>div :nth-child(1)').click()   #点击OK

driver.find_element(By.ID,'customer').click()      #点击客户
driver.find_element(By.XPATH,'//tbody[@id="datas"]/tr[3]/td[1]/input[1]').click()   #选择客户
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message"]+div>div :nth-child(1)').click()  #点击OK

driver.find_element(By.ID,'owner_name').click()     #点击负责人
driver.find_element(By.XPATH,'//tbody[@id="d_content"]/tr[3]/td[1]/input').click()  #选择负责人
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message3"]+div>div :nth-child(1)').click()  #点击OK

driver.find_element(By.ID,'price').clear()     #清空收款金额框
driver.find_element(By.ID,'price').send_keys("10000") #输入收款金额

driver.find_element(By.ID,'pay_time').send_keys("2020-07-23")  #输入日期
driver.find_element(By.XPATH,'//textarea[@class="span6" and @name="description"]').send_keys("123321") #输入描述

driver.find_element(By.XPATH,'//input[@value="保存并新建"]').click()   #点击保存并新建
time.sleep(2)
driver.quit()