"""Tests"""
import pytest
from otus_selenium.models.utility_methods import create_list, \
    edit_items_kotlin, edit_items_cat, delete_items


@pytest.mark.usefixtures('product_page_add')
@pytest.mark.usefixtures('product_page_choice')
@pytest.mark.usefixtures('product_page_waiting')
@pytest.mark.usefixtures('login_for_test')
@pytest.mark.usefixtures('open_login_for_test')
class TestProductPage:
    """Test class"""

    def test_current_page(self, driver):
        """Test page"""
        assert 'product&user_token' in driver.current_url

    def test_check_item(self, driver):
        """Check item"""
        listoc = create_list(driver)
        assert "Kotlin" in listoc

    def test_edit_item(self, driver):
        """Edit"""
        listoc = create_list(driver)
        edit_items_kotlin(driver, listoc)
        listoc = create_list(driver)
        assert "Cat" in listoc
        edit_items_cat(driver, listoc)
        listoc = create_list(driver)
        assert "Kotlin" in listoc

    def test_delete_item(self, driver):
        """Delete"""
        listoc = create_list(driver)
        delete_items(driver, listoc)
        new_list = create_list(driver)
        assert 'Kotlin' not in new_list
