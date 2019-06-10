"""Download"""
import os
import time

import pytest


@pytest.mark.usefixtures('download_page_choice')
# @pytest.mark.usefixtures('page_waiting')
@pytest.mark.usefixtures('login_for_test')
@pytest.mark.usefixtures('open_login_for_test')
class TestDownloadPage:
    """DownloadTest"""

    @pytest.mark.usefixtures('action_with_download')
    def test_add_image(self, driver):
        """Add images"""
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'text.txt')
        input_manager = driver.find_element_by_id('button-upload')
        # input_manager = driver.find_element_by_xpath('//*[@id="form-download"]/div[2]/div/div/span')
        # input_manager = driver.find_element_by_id('input-filename')
        input_manager.send_keys(filename)
        # driver.find_element_by_xpath('//*[@id="form-download"]/div[2]/div/div/span').click()
        time.sleep(5)
        print(filename)
