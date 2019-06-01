"""Locators"""
from selenium.webdriver.common.by import By


class BaseLocators:
    """Base Locators"""
    # PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    PRIMARY_BUTTON = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button')
    PANEL_TITLE = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[1]/h1/text()')
    CLOSE_BUTTON = (By.CLASS_NAME, 'close')
    LOGOUT = (By.CLASS_NAME, 'fa fa-sign-out')
    CATALOG = (By.ID, 'menu-catalog')
    # PRODUCTS = (By.XPATH, '/html/body/div[1]/nav/ul/li[2]/ul/li[2]/a')
    PRODUCTS = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')


class LoginPageLocators:
    """Login"""
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    HREF_OPENCART = (By.XPATH, '//*[@id="footer"]/a')
    FORGOT_PASS = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/form/div[2]/span/a')


class ProductsPageLocators:
    """Products"""
    # ADD_NEW = (By.CLASS_NAME, 'btn btn-primary')
    # ADD_NEW = (By.XPATH, '/html/body/div/div/div[1]/div/div/a')
    ADD_NEW = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    # DELETE = (By.CLASS_NAME, 'fa fa-trash-o')
    DELETE = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')
    # SAVE = (By.CLASS_NAME, 'fa fa-save')
    SAVE = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/button')
    PRODUCT_NAME = (By.ID, 'input-name1')
    META_TAG_TITLE = (By.ID, 'input-meta-title1')
    MODEL = (By.ID, 'input-model')
    PRICE = (By.ID, 'input-price')
    GENERAL = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[1]/a')
    DATA = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[2]/a')
    # CHECK_BOX = (By.NAME, 'selected[]')
    CHECK_BOX = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input')
    FIRST_EDIT_BUTTON = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr[1]/td[8]/a')
    HREF_PRODUCT = (By.XPATH, '//*[@id="content"]/div[1]/div/ul/li[2]/a')
    PRODUCT_LINK = (By.XPATH, '//*[@id="content"]/div[1]/div/ul/li[2]/a')
