import time
import unittest

from driver.browser import chrome_driver
from page.client_page import Client, Client1
from page.login_page import LoginCase


class Clients(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver
        li = LoginCase(self.driver)
        li.login("admin", "banxian123")

    def tearDown(self):
        self.driver.quit()
    def test_catclient(self):
        '''查看客户'''
        cc = Client(self.driver)
        res = cc.cat_client()
        self.assertEqual("分享", res)
    def test_addc(self):
        ''''添加客户放入客户池'''
        ac = Client(self.driver)
        res1 = ac.add_client("胡伟4号")
        self.assertIn("添加客户成功", res1)
    def test_addc2(self):
        '''添加客户不放入客户池'''
        ac2 = Client(self.driver)
        res2 = ac2.add_client2("huwei4号")
        self.assertIn("添加客户成功", res2)
    def test_vimc(self):
        '''编辑客户'''
        vim = Client1(self.driver)
        res3 = vim.vim_client("hw4号")
        self.assertIn("客户编辑成功", res3)
    # def test_flow(self):
    #     self.



if __name__ == '__main__':
    unittest.main()
