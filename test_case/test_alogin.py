import unittest

from driver.browser import chrome_driver
from lib.data_lib import read_txt
from page.login_page import LoginCase


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        lg = LoginCase(self.driver)
        read = read_txt(r"D:\git_root\5kCRM\data\user.txt")
        username = read[0][0]
        password = read[0][1]
        shiji = lg.login(username,password)

        self.assertEqual("http://192.168.1.120/index.php?m=dynamic&a=index", shiji)


if __name__ == '__main__':
    unittest.main()
