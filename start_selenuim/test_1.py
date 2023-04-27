import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from start_selenuim import link
from selenium.webdriver.chrome.options import Options as chrome_options
import time


def start_driver():
    options = chrome_options()
    options.add_argument('chrome')  # use headless if you don`t need UI
    options.add_argument('--start-maximized')  # open window
    driver = webdriver.Chrome(executable_path='C:\QA\ChromeDriver\chromedriver.exe', options=options)

    return driver


# test input, click,
# @pytest.mark.usefixtures('get_webdriver')
def test_input_click():
    driver = start_driver()
    driver.get(link.URL)
    input_line = driver.find_element(By.XPATH, "//div[@class='header-bottom']//input[@class='quick-search-input']")
    input_line.send_keys("Samsung")
    driver.find_element(By.XPATH, "//input[@class='search-button-first-form']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//a[@data-to-category='298']").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div[5]/div/a").click()
    driver.find_element(By.XPATH, "//a[@data-filter='40905-86061936500']").click()
    driver.find_element(By.LINK_TEXT, 'Показати').click()
    #items = driver.find_elements(By.TAG_NAME, "h3")
    #items = driver.find_elements(By.XPATH, "//div[@class='br-pp-ipd-shown']//a[@itemprop='url']")
    #items = driver.find_elements(By.PARTIAL_LINK_TEXT, "телефон")
    items = driver.find_elements(By.XPATH, "//div[@class='col-md-4']//div[@class='br-pp']//div[@class='br-static']//div[@class='description-wrapper']//h3[@class='br-pp-desc']//a[@itemprop='url']")
    #a = "//div[@itemprop='itemListElement']"
    print(len(items))

    for item in items:
        print(item.text)
        #assert "Samsung Galaxy S23 Ultra" in item.text



    #time.sleep(4)




    # driver.quit()




