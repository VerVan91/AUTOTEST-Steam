from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utils.DataUtils import DataUtils


class HomePage(BasePage):
    PRIVACY_POLICY_LINK = (By.XPATH, "//div[@id='footer_text']//a[contains(@href,'privacy_agreement')]")
    HOME_PAGE_UNIQUE = (By.ID, "home_maincap_v7")
    SEARCH_FIELD = (By.ID, "store_nav_search_term")
    SEARCH_START = (By.XPATH, "//*[@id='store_search_link']//img")

    def is_homepage(self):
        return self.is_visible(self.HOME_PAGE_UNIQUE)

    def scroll_to_privacy(self):
        self.scroll_to(self.PRIVACY_POLICY_LINK)

    def click_privacy(self):
        self.do_click(self.PRIVACY_POLICY_LINK)

    def search_game_send_keys(self):
        search_field = self.get_element(self.SEARCH_FIELD)
        search_field.send_keys(DataUtils.test_data_json()['search_request'])

    def search_game_click(self):
        search_start_icon = self.get_element(self.SEARCH_START)
        search_start_icon.click()
