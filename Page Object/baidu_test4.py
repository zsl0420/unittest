from baidu_page import BaiduPage
from time import sleep
import unittest
from selenium import webdriver

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.base_url = "http://www.baidu.com"
        cls.driver = webdriver.Firefox()

    # 测试用例1
    def test_baidu_search_case1(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input("selenium")
        bd.search_button()

    #测试用例2
    def test_baidu_search_case2(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input("unittest")
        bd.search_button()

    # 测试用例3
    def test_baidu_search_case3(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input("page object")
        bd.search_button()
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)