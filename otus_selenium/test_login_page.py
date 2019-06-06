"""Tests"""
import pytest


@pytest.mark.usefixtures('login_page')
class TestLoginPage:
    """Test class"""

    @pytest.mark.usefixtures('login')
    @pytest.mark.usefixtures('open_login_page')
    def test_login(self, driver):
        """Test login"""
        assert 'dashboard' in driver.current_url

    @pytest.mark.usefixtures('wrong_login')
    @pytest.mark.usefixtures('open_login_page')
    def test_wrong_login(self, driver):
        """Test wrong login"""
        assert 'index.php' in driver.current_url

    @pytest.mark.usefixtures('empty_login')
    @pytest.mark.usefixtures('open_login_page')
    def test_empty_fields(self, driver):
        """Test empty field"""
        assert driver.title

    @pytest.mark.usefixtures('href_opencart')
    @pytest.mark.usefixtures('open_login_page')
    def test_href_opencart(self, driver):
        """Test href opencart"""
        assert 'opencart.com' in driver.current_url

    @pytest.mark.usefixtures('forgot_pass')
    @pytest.mark.usefixtures('open_login_page')
    def test_forgot_pass(self, driver):
        """Test forgot pass"""
        assert driver.find_element_by_id('input-email')
