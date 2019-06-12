"""Clouds"""
import pytest
from selenium import webdriver


@pytest.fixture
def bro_clouds():
    """Cap for cloud"""
    desired_cap = {
     'browser': 'Chrome',
     'browser_version': '65.0',
     'os': 'Windows',
     'os_version': '10',
     'resolution': '1024x768',
     'name': 'Bstack-[Python] Sample Test'
    }

    driver = webdriver.Remote(
        command_executor='http://maslovyury1:kEywtC7gUdpbqMP1xDAx@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    return driver


def test_clouds(bro_clouds):
    """Test for cloud"""
    bro_clouds.get("http://www.google.com")
    if not "Google" in bro_clouds.title:
        raise Exception("Unable to load google page!")
    elem = bro_clouds.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.submit()
    # print driver.title
    bro_clouds.quit()
