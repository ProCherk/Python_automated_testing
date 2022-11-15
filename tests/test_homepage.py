import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, "globalSearchInputField")

        #wait = WebDriverWait(driver, 15, 0.3)  # driver, time, period
