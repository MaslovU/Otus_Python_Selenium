import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    """Fixture"""
    w_d = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities={'browserName': 'сhrome'})
    # w_d = webdriver.Remote('http://127.0.0.1:4444/wd/hub', 'browserName= Chrome')

    request.addfinalizer(w_d.quit)
    return w_d


def test_grid(chrome_browser):
    """Test greed"""
    chrome_browser.get('https://google.com')
    if not 'Google' in chrome_browser.title:
        raise Exception('Unable to load google page!')
