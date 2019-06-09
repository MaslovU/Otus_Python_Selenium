"""Pages"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        """Init"""
        self.driver = driver

    def _get_all_attribute_(self, element):
        """Get all attribute"""
        return self.driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index'
            '{ items[arguments[0].attributes[index].name] = '
            'arguments[0].attributes[index].value }; return items;',
            element)

    @staticmethod
    def _get_attribute_(element, attribute):
        """Get attribute"""
        return element.get_attribute(attribute)

    @staticmethod
    def _get_css_attribute_(element, prop):
        """Get CSS"""
        return element.value_of_css_property(prop)

    def _find_and_clear_element_(self, by, value):
        """Find and clear"""
        element = self.driver.find_element(by, value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    @staticmethod
    def _clear_element_(element):
        """Clear"""
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def _wait_element_(self, by, value, delay=25):
        """Wait"""
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def _wait_element_in_other_element_(element, by, value, delay=25):
        """In other"""
        try:
            WebDriverWait(element, delay).until(EC.presence_of_element_located((by, value)))
            elem = element.find_element(by, value)
            return elem
        except TimeoutException:
            return False
