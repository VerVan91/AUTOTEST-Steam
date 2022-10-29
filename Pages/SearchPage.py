from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    SEARCH_PAGE_UNIQUE = (By.XPATH, "//div[@class='searchbar_left']")
    SEARCH_PAGE_BOX = (By.ID, "term")
    SEARCH_PAGE_BOX_ATTRIBUTE = 'value'
    BUTTON_SEARCH_START = (By.XPATH, "//button[contains(@type,'submit')]")
    NAME_IN_LIST = (
        By.XPATH, "//div[@id='search_resultsRows']//a[contains(@class, 'search_result_row')]//span[@class='title']")
    ITEM_PLATFORMS_ATTRIBUTE = "class"
    RELEASE_DATE = (By.XPATH, "(//*[contains(@class, 'search_released')])")
    REVIEW_RESULT = (By.XPATH, "(//*[contains(@class, 'search_review_summary')])")
    REVIEW_RESULT_ATTRIBUTE = 'data-tooltip-html'
    PRICE = (By.XPATH, "(//*[contains(@class, 'search_price')])")

    def is_search_page(self):
        return self.is_visible(self.SEARCH_PAGE_UNIQUE)

    def compare_search_box_and_request(self):
        return self.get_param_attribute(self.SEARCH_PAGE_BOX, self.SEARCH_PAGE_BOX_ATTRIBUTE)[0]

    def get_names(self):
        return self.get_param_text(self.NAME_IN_LIST)

    def get_platforms(self, number):
        xpath = f"//a[contains(@class, 'search_result_row')][{number+1}]//span[contains(@class, 'platform_img')]"
        res = []
        for element in self.get_param_attribute((By.XPATH, xpath), self.ITEM_PLATFORMS_ATTRIBUTE):
            res.append(element[13:])
        return res

    def get_release_dates(self):
        return self.get_param_text(self.RELEASE_DATE)

    def get_review_results(self):
        return self.get_param_attribute(self.REVIEW_RESULT, self.REVIEW_RESULT_ATTRIBUTE)

    def get_prices(self):
        return self.get_param_text(self.PRICE)

    def get_one_game_info(self, number):
        name = self.get_names()[number]
        platform = self.get_platforms(number)
        release_date = self.get_release_dates()[number]
        review_result = self.get_review_results()[number]
        price = self.get_prices()[number]
        return name, platform, release_date, review_result, price

    def first_name_in_list(self):
        first_item_name = self.get_element(self.NAME_IN_LIST).text
        return first_item_name

    def search_second_name_send_keys(self, second_game_text):
        search_box = self.get_element(self.SEARCH_PAGE_BOX)
        search_box.clear()
        search_box.send_keys(second_game_text)

    def search_second_name_click(self):
        btn_search_start = self.get_element(self.BUTTON_SEARCH_START)
        btn_search_start.click()
