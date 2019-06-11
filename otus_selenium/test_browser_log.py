"""Test browser log adn proxy"""


def test_logging_browser(driver):
    """test log browser"""
    driver.get('https://otus.ru')
    listoc = driver.get_log('performance')
    for l in listoc:
        print(l)


def test_proxy(driver, my_proxy):
    """test log browser"""
    driver.get('https://otus.ru')
    print('')
    print(my_proxy.har)
