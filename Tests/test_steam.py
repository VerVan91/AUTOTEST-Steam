import pytest
from Pages.SearchPage import SearchPage
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
from Pages.PrivacyPage import PrivacyPage
from Utils.DataUtils import DataUtils
from Utils.SearchingData import SearchingData
from Utils.Utils import Utils


@pytest.mark.usefixtures('setup')
class TestSteam:

    def test_privacy_policy(self):
        home_page = HomePage()
        assert home_page.is_homepage(), "This page is NOT Homepage"
        home_page.scroll_to_privacy()
        home_page.click_privacy()
        base_page = BasePage()
        base_page.switch_to_new_open_tab()
        privacy_page = PrivacyPage()
        assert privacy_page.is_langs_list_displayed(), "Switch language elements list are NOT displayed"
        assert privacy_page.are_all_langs() == set(DataUtils.test_data_json()['supported_langs']), "Supported all languages"
        assert privacy_page.is_policy_revision_ok(), "Policy revision signed in NOT the current year."

    def test_game_search(self):
        home_page = HomePage()
        assert home_page.is_homepage(), "This page is NOT Homepage"
        home_page.search_game_send_keys()
        home_page.search_game_click()
        search_page = SearchPage()
        assert search_page.is_search_page(), "This page is NOT Search page"
        assert search_page.compare_search_box_and_request() == DataUtils.test_data_json()['search_request'], "This is not searching request"

        assert search_page.first_name_in_list() == DataUtils.test_data_json()['search_request'], "The first name is NOT equal to searched name"
        first_game_first_run = SearchingData(*search_page.get_one_game_info(0))
        second_game_first_run = SearchingData(*search_page.get_one_game_info(1))

        search_page.search_second_name_send_keys(second_game_first_run.name)
        search_page.search_second_name_click()

        assert search_page.compare_search_box_and_request() == second_game_first_run.name, "Search box on result page doesn't contain searched name"

        first_game_second_run_number = Utils.searching_equal_games(search_page.get_names(), first_game_first_run.name, second_game_first_run.name)[0]
        second_game_second_run_number = Utils.searching_equal_games(search_page.get_names(), first_game_first_run.name, second_game_first_run.name)[1]

        first_game_second_run = SearchingData(*search_page.get_one_game_info(first_game_second_run_number))
        second_game_second_run = SearchingData(*search_page.get_one_game_info(second_game_second_run_number))

        assert first_game_first_run == first_game_second_run, "All data FIRST game are NOT matched"
        assert second_game_first_run == second_game_second_run, "All data SECOND game are NOT matched"
