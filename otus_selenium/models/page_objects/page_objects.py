"""Page_Objects"""
from otus_selenium.models.page import BasePage
from otus_selenium.models.locator import BaseLocators, LoginPageLocators, ProductsPageLocators


class LoginPage(BasePage):
    """Base Page"""
    def set_username(self, username):
        """User name"""
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        """Password"""
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        """Login"""
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def title(self):
        """Title"""
        self.driver.find_element(*BaseLocators.PANEL_TITLE)
    #
    # def clear_password(self):
    #     """Clear element"""
    #     self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

    def close_button(self):
        """Close button"""
        self.driver.find_element(*BaseLocators.CLOSE_BUTTON).click()

    def logout(self):
        """Logout"""
        self.driver.find_element(*BaseLocators.LOGOUT).click()

    def href_opencart(self):
        """Href open card"""
        self.driver.find_element(*LoginPageLocators.HREF_OPENCART).click()

    def forgot_pass(self):
        """Forgot pass"""
        self.driver.find_element(*LoginPageLocators.FORGOT_PASS).click()


class ProductsPage(BasePage):
    """Products Page"""

    def catalog_navigation(self):
        """Catalog"""
        self.driver.find_element(*BaseLocators.CATALOG).click()

    def products_navigation(self):
        """Products"""
        self.driver.find_element(*BaseLocators.PRODUCTS).click()

    def products_navigation_two(self):
        """Products"""
        self.driver.find_element(*BaseLocators.PRODUCTS).click()

    def add_new_item_button(self):
        """Add new"""
        self.driver.find_element(*ProductsPageLocators.ADD_NEW).click()

    def add_product_name(self, product_name):
        """Product name"""
        self.driver.find_element(*ProductsPageLocators.PRODUCT_NAME).send_keys(product_name)

    def clean_product_name(self):
        """Clean"""
        self.driver.find_element(*ProductsPageLocators.PRODUCT_NAME).clear()

    def add_meta_tag(self, meta_tag):
        """Meta tag"""
        self.driver.find_element(*ProductsPageLocators.META_TAG_TITLE).send_keys(meta_tag)

    def data_tag(self):
        """Data tag"""
        self.driver.find_element(*ProductsPageLocators.DATA).click()

    def model_of_item(self, model):
        """Model"""
        self.driver.find_element(*ProductsPageLocators.MODEL).send_keys(model)

    def price_of_item(self, price):
        """Price"""
        self.driver.find_element(*ProductsPageLocators.PRICE).send_keys(price)

    def save_button(self):
        """Save"""
        self.driver.find_element(*ProductsPageLocators.SAVE).click()

    def check_box(self):
        """Check box"""
        self.driver.find_element(*ProductsPageLocators.CHECK_BOX).click()

    def delete_button(self):
        """Delete"""
        self.driver.find_element(*ProductsPageLocators.DELETE).click()

    def edit_button(self):
        """Edit"""
        self.driver.find_element(*ProductsPageLocators.FIRST_EDIT_BUTTON).click()

    def href_product(self):
        """product"""
        self.driver.find_element(*ProductsPageLocators.HREF_PRODUCT).click()

    def product_link(self):
        self.driver.find_element(*ProductsPageLocators.PRODUCT_LINK).click()
