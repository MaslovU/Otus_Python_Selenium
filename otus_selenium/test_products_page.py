"""Tests"""
import pytest
from otus_selenium.models.utility_methods import create_list, \
    edit_items_kotlin, edit_items_cat, delete_items


@pytest.mark.usefixtures('product_page_add')
@pytest.mark.usefixtures('product_page_choice')
@pytest.mark.usefixtures('page_waiting')
@pytest.mark.usefixtures('login_for_test')
@pytest.mark.usefixtures('open_login_for_test')
class TestProductPage:
    """Test class"""

    def test_current_page(self, driver):
        """Test page"""
        bad_list = []
        listoc = create_list(driver)
        for i in listoc:
            if i == "Kotlin":
                bad_list.append(i)
        if len(bad_list) > 1:
            delete_items(driver, listoc)
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

    # @pytest.mark.usefixtures('add_images')
    # @pytest.mark.usefixtures('action_with_image')
    # def test_add_three_images(self, driver):
    #     """Add images"""
    #     time.sleep(2)
    #     dirname = os.path.dirname(__file__)
    #     filename = os.path.join(dirname, 'image3.jpg')
    #     input_manager = driver.find_element_by_css_selector('button-upload')
    #     # driver.find_element_by_id('button-upload').click()
    #     # input_manager = driver.find_element_by_id('//*[@id="form-upload"]')
    #     input_manager.send_keys(filename)
    #
    # def test_delete_images(self):
    #     """Delete images"""
    #     pass
