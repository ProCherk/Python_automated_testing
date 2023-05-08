import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from start_selenuim import link
from selenium.webdriver.chrome.options import Options as chrome_options


def start_driver():
    options = chrome_options()
    options.add_argument('chrome')  # use headless if you don`t need UI
    options.add_argument('--start-maximized')  # open window
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path='C:\QA\ChromeDriver\chromedriver.exe', options=options)

    return driver


def test_to_assert():
    driver = start_driver()
    driver.get(link.URL_ROZETKA)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Побутова").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Холодильники").click()
    time.sleep(3)

    try:
        driver.find_element(By.XPATH, "//span[@class='exponea-close-cross']").click()
    except NoSuchElementException:
        pass

    # filter products
    min = driver.find_element(By.XPATH, "//input[@formcontrolname='min']")
    min.clear()
    min.send_keys('5000')
    max = driver.find_element(By.XPATH, "//input[@formcontrolname='max']")
    max.clear()
    max.send_keys('25000')
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    count = 1

    while True: # i cant finish test, error 404 at 2 page on random item
        next_button = driver.find_element(By.XPATH, "//a[@title='До наступної сторінки']")
        if next_button.get_attribute('href') is not None:
            prices = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
            numb_of_item = 1
            price = ''
            for item in prices:  # check prices of the selected product
                test_data = str(item.text)  # transform data to int type
                # print(item.text)
                for i in range(len(test_data)):
                    if test_data[i].isnumeric():
                        price += test_data[i]
                # print(price)
                assert int(price) > 5000, f"The price of item is less than 5000 - {item}"
                assert int(price) < 25000, f"The price of item is more than 25000 - {item}"
                price = ""
                print(numb_of_item)
                numb_of_item += 1

            next_button.click()
            print(count)
            count += 1
        else:
            break

        # print(len(prices))
