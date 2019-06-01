"""Utility methods"""


def create_list(driver):
    """Create list"""
    rowcount = len(driver.find_elements_by_xpath('//*[@id="form-product"]/div/table/tbody/tr'))
    listoc = []
    for i in range(1, rowcount+1):
        elem = driver\
            .find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(i) + ']/td[3]')
        listoc.append(elem.text)
    return listoc


def edit_items_kotlin(driver, listoc):
    """Edit item"""
    index = listoc.index('Kotlin')
    driver.\
        find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(index + 1) + ']/td[8]/a').click()
    driver.find_element_by_id('input-name1').clear()
    driver.find_element_by_id('input-name1').send_keys('Cat')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/button').click()


def edit_items_cat(driver, listoc):
    """Edit Cat"""
    index = listoc.index('Cat')
    driver.\
        find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[' + str(index + 1) + ']/td[8]/a') \
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
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button[3]').click()
    driver.switch_to_alert().accept()
    driver.refresh()
