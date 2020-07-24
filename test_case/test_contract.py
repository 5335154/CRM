import unittest

from driver.browser import chrome_driver
from page.contract_page import ContractCase
from page.login_page import LoginCase


class ContractTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_contract(self):
        dl = LoginCase(self.driver)
        dl.login("admin","banxian123")

        cc = ContractCase(self.driver)
        shiji = cc.add_preservation()

        self.assertIn("创建合同成功", shiji)


if __name__ == '__main__':
    unittest.main()
