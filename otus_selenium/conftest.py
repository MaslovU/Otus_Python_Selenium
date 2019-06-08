"""Conftest"""
import sys
import time
import pytest
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from otus_selenium.models.page_objects.page_objects import *


CHROMEDRIVERPATH = "/home/yury/PycharmProjects/Otus_Selenium/otus_selenium/chromedriver"
FIREFOXDRIVERPATH = '/home/yury/PycharmProjects/Otus_Selenium/otus_selenium/geckodriver'


def pytest_addoption(parser):
    """Add option"""
    parser.addoption(
        "--name_browser",
        action="store",
        default="chrome",
        help="my option: chrome or firefox"
    )
    parser.addoption(
        "--urlopt",
        action="store",
        default="http://localhost/",
        help="default url address localhost/opencart/"
    )
    parser.addoption(
        "--time_out",
        action="store",
        default=5,
        help="default time for waiting 5 sec"
    )


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Driver"""
    browser = request.config.getoption("--name_browser")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        options = FirefoxOptions()
        options.add_argument("--start-fullscreen")
        # options.add_argument("--headless")
        w_d = webdriver.Firefox(firefox_options=options,
                                executable_path=FIREFOXDRIVERPATH)
        w_d.maximize_window()
    elif browser == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        options = ChromeOptions()
        options.add_argument("--start-fullscreen")
        # options.add_argument("--headless")
        w_d = webdriver.Chrome(chrome_options=options,
                               executable_path=CHROMEDRIVERPATH)
        w_d.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    w_d.set_page_load_timeout(100)
    yield w_d
    w_d.quit()


@pytest.fixture(scope="function")
def open_login_page(driver, request):
    """Open login page"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--urlopt"), url]))


@pytest.fixture(scope="module")
def open_login_for_test(driver, request):
    """Open login page"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--urlopt"), url]))


@pytest.fixture(scope='module')
def login_page(driver):
    """Login page"""
    return LoginPage(driver)


@pytest.fixture(scope='function')
def login(login_page):
    """Login"""
    login_page.set_username('admin')
    login_page.set_password('admin')
    login_page.login()
    login_page.close_button()
    time.sleep(1)


@pytest.fixture(scope='module')
def login_for_test(login_page):
    """Login"""
    login_page.set_username('admin')
    login_page.set_password('admin')
    login_page.login()
    login_page.close_button()
    time.sleep(5)


@pytest.fixture(scope='function')
def wrong_login(login_page):
    """Wrong login"""
    login_page.set_username('badadmin')
    login_page.set_password('admin')
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope='function')
def empty_login(login_page):
    """Empty login"""
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope='function')
def href_opencart(login_page):
    """Href opencart"""
    login_page.href_opencart()
    time.sleep(5)


@pytest.fixture(scope='function')
def forgot_pass(login_page):
    """Forgot pass"""
    login_page.forgot_pass()
    time.sleep(5)


@pytest.fixture(scope='module')
def products_page(driver):
    """Product page"""
    return ProductsPage(driver)


@pytest.fixture(scope='module')
def product_page_choice(products_page):
    """Page choice"""
    products_page.catalog_navigation()
    products_page.products_navigation()


@pytest.fixture(scope='class')
def product_page_add(products_page):
    """Page add"""
    products_page.add_new_item_button()
    products_page.add_product_name('Kotlin')
    products_page.add_meta_tag('abba2')
    products_page.data_tag()
    products_page.model_of_item('1985')
    products_page.price_of_item('11')
    products_page.save_button()


@pytest.fixture(scope='module')
def product_page_waiting(request):
    time_of_waiting = request.config.getoption("--time_out")
    time.sleep(time_of_waiting)


@pytest.fixture(scope='function')
def action_with_image(products_page):
    products_page.edit_button()
    products_page.image_button()
    products_page.click_on_image()


@pytest.fixture()
def add_images(products_page, driver):
    products_page.button_edit_image()


@pytest.fixture()
def delete_image(products_page, driver):
    products_page.button_delete_image()
