"""Conftest"""
import logging
import sys
import time
import urllib.parse
import platform

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
# from browsermobproxy import Server
from otus_selenium.models.page_objects.page_objects import *
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

import sqlite3
from otus_selenium.sqlite3 import sqlite3_mas


conn = sqlite3.connect('/home/yury/maslov.db')
cursor = conn.cursor()


CHROMEDRIVERPATH = "/home/yury/PycharmProjects/Otus_Selenium/otus_selenium/chromedriver"
FIREFOXDRIVERPATH = '/home/yury/PycharmProjects/Otus_Selenium/otus_selenium/geckodriver'

# базовые настройки для логирования
# logging.basicConfig(filename='/home/yury/PycharmProjects/selenium_otus/otus_selenium/lolo.log', level=logging.INFO)
logging.basicConfig(level=logging.INFO)

# настройка логирования http запросов через proxy
# server = Server(r'/home/yury/Desktop/browsermob-proxy-2.1.4/bin/browsermob-proxy')
# server.start()

# for test proxy
# @pytest.fixture(scope='session')
# def my_proxy():
#     """My proxy"""
#     proxy = server.create_proxy()
#     proxy.new_har()
#     return proxy


class MyListener(AbstractEventListener):
    """My listener"""

    def before_find(self, by, value, driver):
        """for logs"""
        log = 'Message before find'
        sqlite3_mas(log)
#
#     def after_find(self, by, value, driver):
#         """for logs"""
#         logging.info('Message after find')
#
#     def before_click(self, element, driver):
#         """for logs"""
#         logging.info("Start click")
#
#     def after_click(self, element, driver):
#         """for logs"""
#         logging.info('Message after click')
#
#     def before_quit(self, driver):
#         """for logs"""
#         logging.info('before quit')
#
#     def after_quit(self, driver):
#         """for logs"""
#         logging.info('by!')
#
#     def on_exception(self, exception, driver):
#         """for logs"""
#         driver.save_screenshot('/home/yury/PycharmProjects/selenium_otus/otus_selenium/screenshots/exceptions.png')


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
    # for test proxy (check all comments)
    # def driver(request, my_proxy):
    """Driver"""
    browser = request.config.getoption("--name_browser")
    if browser == 'firefox':
        # for logging
        d = webdriver.DesiredCapabilities.FIREFOX
        d['loggingPrefs'] = {'performance': 'ALL'}
        # for usial tests
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        options = FirefoxOptions()
        # for test proxy
        # url = urllib.parse.urlparse(my_proxy.proxy).path
        # options.add_argument('--proxy-server=%s' % url)
        options.add_argument("--start-fullscreen")
        options.add_argument("--headless")
        w_d = EventFiringWebDriver(webdriver.Firefox(firefox_options=options,
                                                     executable_path=FIREFOXDRIVERPATH),
                                   MyListener())
        w_d.maximize_window()
    elif browser == 'chrome':
        # for logging
        d = webdriver.DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'performance': 'ALL'}
        # for usial tests
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        options = ChromeOptions()
        # for test proxy
        # url = urllib.parse.urlparse(my_proxy.proxy).path
        # options.add_argument('--proxy-server=%s' % url)
        options.add_argument("--start-fullscreen")
        options.add_argument("--headless")
        w_d = EventFiringWebDriver(webdriver.Chrome(chrome_options=options,
                                                    executable_path=CHROMEDRIVERPATH,
                                                    desired_capabilities=d),
                                   MyListener())
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
    time.sleep(1)


@pytest.fixture(scope='module')
def login_for_constructor(login_page):
    """Login"""
    login_page.set_username('demo')
    login_page.set_password('demo')
    login_page.login()
    time.sleep(1)


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


@pytest.fixture(scope='function')
def product_page_choice_pro(products_page):
    """Page choice"""
    products_page.catalog_navigation()
    products_page.products_navigation_pro()


@pytest.fixture(scope='module')
def product_page_add(products_page):
    """Page add"""
    products_page.add_new_item_button()
    products_page.add_product_name('Kotlin')
    products_page.add_meta_tag('abba2')
    products_page.data_tag()
    products_page.model_of_item('1985')
    products_page.price_of_item('11')
    products_page.save_button()


@pytest.fixture(scope='function')
def product_page_add_pro(products_page):
    """Page add"""
    products_page.add_new_item_button()
    products_page.add_product_name('Abba')
    products_page.data_tag()
    products_page.model_of_item('1985')
    products_page.price_of_item('11')
    products_page.save_button()


@pytest.fixture(scope='module')
def page_waiting(request):
    """For pro"""
    time_of_waiting = request.config.getoption("--time_out")
    time.sleep(time_of_waiting)


@pytest.fixture(scope='function')
def action_with_image(products_page):
    products_page.edit_button()
    products_page.image_button()
    products_page.click_on_image()


@pytest.fixture(scope='function')
def action_with_image_pro(products_page):
    """For pro"""
    products_page.edit_for_pro()
    products_page.image_button()
    products_page.click_on_add_pro()
    products_page.click_on_image_pro()


@pytest.fixture()
def add_images(products_page, driver):
    """Adding"""
    products_page.button_edit_image()


@pytest.fixture()
def delete_image(products_page, driver):
    """Deleting"""
    products_page.button_delete_image()


@pytest.fixture(scope='module')
def download_page(driver):
    """Product page"""
    return DownloadPage(driver)


@pytest.fixture(scope='module')
def download_page_choice(products_page):
    """Download page"""
    products_page.catalog_navigation()
    time.sleep(1)
    products_page.download_navigation()


@pytest.fixture(scope='function')
def action_with_download(download_page):
    """For pro"""
    download_page.add_new_button()
    download_page.download_file_name('image1')


# tow methods for json
@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def extra_json_environment(request, environment_info):
    request.config._json_environment.append(("dist", environment_info[1]))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        # only add this during call instead of during any stage
        report.test_metadata = 'whatever'
        # edit stage metadata
        report.stage_metadata = {
            'lets': 'do it',
            'time': time.time(),

        }
    elif report.when == 'setup':
        report.stage_metadata = {
            'unknown': 'imformation'
        }
    elif report.when == 'teardown':
        report.stage_metadata = {
            'hey': 'by by'
        }


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    linux_dist = platform.linux_distribution()
    python_version = platform.python_version()
    return os_platform, linux_dist, python_version


# for html reports
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         report.extra = extra
#
#
# @pytest.mark.usefixtures("environment_info")
# @pytest.fixture(scope='session', autouse=True)
# def configure_html_report_env(request, environment_info):
#     request.config._metadata.update(
#         {"browser": request.config.getoption("--name_browser"),
#          "address": request.config.getoption("--urlopt"
#          # here can add options to enviroment
#          )})
#     yield
