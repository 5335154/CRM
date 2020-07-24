import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from driver.browser import chrome_driver


class SearchBusinessCase():
    def __init__(self,driver):
        self.driver = driver
        #元素定位符
        self.dw_intosearch = (By.LINK_TEXT, '商机')                                           #进入商机页面
        self.dw_busniness = (By.CSS_SELECTOR, 'ul[class="nav nav-tabs"] :nth-child(2)')      #统计
        self.dw_statistics = (By.CSS_SELECTOR, 'ul[class="nav nav-tabs"] :nth-child(1)')     #商机
        self.dw_mycharge = (By.LINK_TEXT, '我负责的')                                         #我负责的
        self.dw_subordinates_create = (By.LINK_TEXT, '下属创建的')                            #下属创建的
        self.dw_today_contact = (By.LINK_TEXT, '今日需联系')                                  #今日需联系
        self.dw_thirtyday = (By.LINK_TEXT, '30日未联系')                                     #30日未联系
        self.dw_recently_updated = (By.LINK_TEXT, '最近更新')                                 #最近更新
        self.dw_month_contact = (By.LINK_TEXT, '本月需联系')                                  #本月需联系
        self.dw_sevenday = (By.LINK_TEXT, '7日未联系')                                       #7日未联系
        self.dw_recycle = (By.LINK_TEXT, '回收站')                                           #回收站
        self.dw_choiceone = (By.ID, 'field')                                                #选择筛选条件1
        self.dw_choicetwo = (By.ID, 'condition')                                            #选择筛选条件2
        self.dw_keyword = (By.ID, "search")                                                 #输入关键字
        self.dw_dosearch = (By.ID, 'dosearch')                                              #点击搜索


    def ele_into_search(self):
        self.driver.find_element(*self.dw_intosearch).click()      #进入商机页面

    def ele_busniness(self):
        self.driver.find_element(*self.dw_busniness).click()  #统计
        self.driver.save_screenshot("../screenshot/统计.png")

    def ele_statistics(self):
        self.driver.find_element(*self.dw_statistics).click()  #商机
        self.driver.save_screenshot("../screenshot/商机.png")

    def ele_mycharge(self):
        self.driver.find_element(*self.dw_mycharge).click()          #我负责的
        self.driver.save_screenshot("../screenshot/我负责的.png")

    def ele_subordinates_create(self):
        self.driver.find_element(*self.dw_subordinates_create).click()         #下属创建的
        self.driver.save_screenshot("../screenshot/下属创建的.png")

    def ele_today_contact(self):
        self.driver.find_element(*self.dw_today_contact).click()         #今日需联系
        self.driver.save_screenshot("../screenshot/今日需联系.png")

    def ele_thirtyday(self):
        self.driver.find_element(*self.dw_thirtyday ).click()         #30日未联系
        self.driver.save_screenshot("../screenshot/30日未联系.png")

    def ele_recently_updated(self):
        self.driver.find_element(*self.dw_recently_updated).click()           #最近更新
        self.driver.save_screenshot("../screenshot/最近更新.png")

    def ele_month_contact(self):
        self.driver.find_element(*self.dw_month_contact).click()         #本月需联系
        self.driver.save_screenshot("../screenshot/本月需联系.png")

    def ele_sevenday(self):
        self.driver.find_element(*self.dw_sevenday).click()          #7日未联系
        self.driver.save_screenshot("../screenshot/7日未联系.png")

    def ele_recycle(self):
        self.driver.find_element(*self.dw_recycle).click()             #回收站
        self.driver.save_screenshot("../screenshot/回收站.png")

    def ele_choiceone(self):
        ele = self.driver.find_element(*self.dw_choiceone)                      #选择筛选条件1
        select = Select(ele)
        select.select_by_index(3)

    def ele_choicetwo(self):
        ele = self.driver.find_element(*self.dw_choicetwo)                  #选择筛选条件2
        select = Select(ele)
        select.select_by_index(0)

    def ele_keyword(self,keyword):
        self.driver.find_element(*self.dw_keyword).send_keys(keyword)         #输入关键字

    def ele_dosearch(self):
        self.driver.find_element(*self.dw_dosearch).click()                 #点击搜索
        self.driver.save_screenshot("../screenshot/搜索结果.png")

    def search(self,keyword):
        self.ele_into_search()
        self.ele_busniness()
        self.ele_statistics()
        self.ele_mycharge()
        self.ele_subordinates_create()
        self.ele_today_contact()
        self.ele_thirtyday()
        self.ele_recently_updated()
        self.ele_month_contact()
        self.ele_sevenday()
        self.ele_recycle()
        self.ele_choiceone()
        self.ele_choicetwo()
        self.ele_keyword(keyword)
        self.ele_dosearch()
        time.sleep(2)
        shiji = self.driver.current_url
        return shiji

# search = SearchBusinessCase()
# search.search()