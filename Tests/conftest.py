import pytest

from Tests.WebDriver import WebDriver
from Utils.DataUtils import DataUtils


@pytest.fixture
def setup(request):
    driver = WebDriver.get_driver()
    if request.cls is not None:
        request.cls.__driver = driver
    driver.get(DataUtils.test_data_json()['url'])
    yield driver
    driver.quit()
    WebDriver.__del__()
