from Config.BrowserFactory import BrowserFactory
from Utils.DataUtils import DataUtils


class WebDriver:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = BrowserFactory.get_browser(DataUtils.config_data_json()['browser_name'])
        return cls.__driver

    @classmethod
    def __del__(cls):
        cls.__driver = None
