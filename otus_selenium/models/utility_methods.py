"""Utility methods"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def create_list(driver):
    """Create list"""
    row = driver.find_elements_by_xpath('//*[@id="form-product"]/div/table/tbody/tr')
    rowcount = len(row)
    if rowcount <= 0:
        raise ValueError("List shouldn't be empty")
    listoc = []
    for i in range(1, rowcount+1):
        elem = driver\
            .find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(i) + ']/td[3]')
        listoc.append(elem.text)
    return listoc


def edit_items_kotlin(driver, listoc):
    """Edit item"""
    global index
    try:
        index = listoc.index('Kotlin')
    except ValueError:
        print('We cannot find element Kotlin')
    driver.\
        find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(index + 1) + ']/td[8]/a').click()
    driver.find_element_by_id('input-name1').clear()
    driver.find_element_by_id('input-name1').send_keys('Cat')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/button').click()


def edit_items_cat(driver, listoc):
    """Edit Cat"""
    index2 = listoc.index('Cat')
    driver.\
        find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(index2 + 1) + ']/td[8]/a') \
        .click()
    driver.find_element_by_id('input-name1').clear()
    driver.find_element_by_id('input-name1').send_keys('Kotlin')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/button').click()


def delete_items(driver, listoc):
    """Delete item"""
    index = listoc.index('Kotlin')
    driver\
        .find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(index + 1) + ']/td[1]/input') \
        .click()
    # driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button[3]').click()
    wait = WebDriverWait(driver, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]'))).click()
    driver.switch_to_alert().accept()
    driver.refresh()


def add_new_image(driver):
    driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="form-product"]/ul/li[9]/a').click()


def create_constructor_list(driver):
    """Constructor list"""
    cons_list = driver.find_elements_by_class_name('item-title')
    listok = []
    for i in cons_list:
        listok.append(i.text)
    return listok
