from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)  # driver, time, period

    def get_selenium_by(self, find_by):
        locating = {'css': By.CSS_SELECTOR}
