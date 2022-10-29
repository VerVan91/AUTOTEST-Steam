from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Utils.DataUtils import DataUtils


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name):
        if browser_name == 'chrome':
            options = Options()
            options.add_argument(DataUtils.config_data_json()['browser_name'])
            options.add_argument(DataUtils.config_data_json()['opening_mode'])
            options.add_argument(DataUtils.config_data_json()['screen_mode'])
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            return driver
        elif browser_name == 'firefox':
            pass
        else:
            raise Exception("No such " + browser_name + " browser exists")
