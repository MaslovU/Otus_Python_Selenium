import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    """Fixture"""
    wd = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})

    request.addfinalizer(wd.quit)
    return wd


def test_grid(chrome_browser):
    """Test greed"""
    chrome_browser.get('https://google.com')
    if not 'Google' in chrome_browser.title:
        raise Exception('Unable to load google page!')
