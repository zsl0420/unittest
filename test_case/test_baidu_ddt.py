import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, data, file_data, unpack

@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.base_url = "http://www.baidu.com"

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)

    # 参数化使用方式一之列表
    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    @unpack
    def test_search1(self, case, search_key):
        print("第一组测试用例:", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化使用方式二之元组
    @data(("case1", "selenium"), ("case2", "ddt"),("case3", "python"))
    @unpack
    def test_search2(self, case, search_key):
        print("第二组测试用例:", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    #参数化使用方式三之字典
    @data({"search_key": "selenium"}, {"search_key": "ddt"}, {"search_key": "python"})
    @unpack
    def test_search3(self, search_key):
        print("第三组测试用例:", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
