import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # use headless if you don`t need UI
    options.add_argument('--start-maximized')  # open window
    options.add_argument('--window-size=1920,1080')  # window size
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='C:\QA\ChromeDriver\chromedriver.exe', options=options)  # get Webdriver from system variables path
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://www.macys.com/"
    if request.cls is not None:  # like if test in class give it driver
        request.cls.driver = driver
    driver.get(url)  # open url
    yield driver
    driver.quit()
