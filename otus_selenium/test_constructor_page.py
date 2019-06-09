"""Constructor"""
import pytest
from selenium.webdriver import ActionChains

from otus_selenium.models.utility_methods import create_constructor_list


@pytest.mark.usefixtures('login_for_constructor')
@pytest.mark.usefixtures('open_login_for_test')
class TestConstructor:
    """Test Constructor"""

    def test_check_product_in_list(self, driver):
        """Check item on position"""
        listok = create_constructor_list(driver)
        item = listok[0]
        assert item != 'Macs'

    def test_move_items(self, driver):
        """Move items"""
        first_el = driver.find_element_by_xpath('//*[@id="custommenu-item-24"]/dl')
        last_el = driver.find_element_by_xpath('//*[@id="custommenu-child-item-77"]/dl/dt')
        action = ActionChains(driver)

        action.drag_and_drop(last_el, first_el).perform()

        listok = create_constructor_list(driver)
        item = listok[0]
        assert item == 'Macs'
