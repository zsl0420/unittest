import unittest
from selenium import webdriver
from time import sleep

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.baidu.com"

    def test_search_key_selenium(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "selenium_百度搜索")

    def test_search_key_unttest(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "unittest_百度搜索")


if __name__ == '__main__':
    unittest.main()
