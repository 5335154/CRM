import unittest

from driver.browser import chrome_driver
from lib.data_lib import read_csv
from page.business_page import BusinessCase
from page.login_page import LoginCase
from page.search_business_page import SearchBusinessCase


class BusinessTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver
        lg = LoginCase(self.driver)
        lg.login("admin", "banxian123")

    def tearDown(self):
        self.driver.quit()

    def test_business(self):
#添加商机
        bus = BusinessCase(self.driver)
        sj = read_csv(r"D:\git_root\5kCRM\data\business.csv")
        busname = sj[5][0]
        yprice = sj[5][1]
        shiji = bus.add_bus_opp("商C",yprice)
        self.assertIn("添加商机成功", shiji)
#搜索商机
        # search = SearchBusinessCase(self.driver)
        # shiti = search.search("大商机")
        # self.assertEqual("http://192.168.1.120/index.php?field=name&condition=contains&search=%E5%A4%A7%E5%95%86%E6%9C%BA&m=business&act=search&daochu=&current_page=&export_limit=&by=deleted",
        #                  shiti)

if __name__ == '__main__':
    unittest.main()
