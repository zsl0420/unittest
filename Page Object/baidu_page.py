class BaiduPage():

    def __init__(self, driver):
        self.driver = driver

    # 封装search_input 和 search_button 方法
    def search_input(self, search_key):
        self.driver.find_element_by_id("kw").send_keys(search_key)

    def search_button(self):
        self.driver.find_element_by_id("su").click()
