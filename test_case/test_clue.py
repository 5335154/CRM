import unittest

from driver.browser import chrome_driver
from page.change_clue import SwichToClient
from page.clue_page import ClueCase
from page.login_page import LoginCase


class ClueTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver
        lg = LoginCase(self.driver)
        lg.login("admin", "banxian123")

    def tearDown(self):
        self.driver.quit()
#添加线索
    def test_aclue(self):
        clue = ClueCase(self.driver)
        jieguo = clue.add_clue("大公司4号","4号联系人")
        self.assertIn("线索添加成功",jieguo)

#转换为客户
    def test_changeclue(self):
        swi = SwichToClient(self.driver)
        shiji = swi.switchclient()
        self.assertIn("添加客户成功",shiji)

if __name__ == '__main__':
    unittest.main()
