from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.WebDriver import WebDriver
from Utils.DataUtils import DataUtils


class BasePage:
    WAIT_TIME = DataUtils.config_data_json()['wait_time']

    def __init__(self):
        self.driver = WebDriver.get_driver()

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).click()

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_elements(self, by_locator):
        elements = WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def get_param_text(self, by_locator):
        elements = self.get_elements(by_locator)
        res = []
        for element in elements:
            res.append(element.text)
        return res

    def get_param_attribute(self, by_locator, by_attribute):
        elements = self.get_elements(by_locator)
        res = []
        for element in elements:
            res.append(element.get_attribute(by_attribute))
        return res

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def scroll_to(self, by_locator):
        action = ActionChains(self.driver)
        element = WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        action.move_to_element(element)
        action.perform()

    def switch_to_new_open_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
