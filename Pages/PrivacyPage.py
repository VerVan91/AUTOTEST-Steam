from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from datetime import date


class PrivacyPage(BasePage):
    SWITCH_LANGUAGES_LIST = (By.ID, "languages")
    SWITCH_LANGUAGES_ITEM = (By.XPATH, "//div[@id='languages']//a[contains(@href, 'privacy_agreement')]")
    POLICY_REVISION_YEAR = (By.XPATH, "//*[@id='newsColumn']/i[last()]")

    def is_langs_list_displayed(self):
        return self.is_visible(self.SWITCH_LANGUAGES_LIST)

    def are_all_langs(self):
        list_langs_links = self.get_elements(self.SWITCH_LANGUAGES_ITEM)
        list_langs = []

        for i in list_langs_links:
            list_langs.append(i.get_attribute('href').split('/')[-2])

        return set(list_langs)

    def is_policy_revision_ok(self):
        current_year = date.today().year
        element = self.get_element(self.POLICY_REVISION_YEAR)
        return str(current_year) in element.text
