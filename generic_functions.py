from selenium.webdriver.support.select import Select

from Setup.Setup_files import driver


def do_click(by_locator):
    driver.find_element(*by_locator).click()

def do_sendkeys(by_locator,keys):
    driver.find_element(*by_locator).send_keys(keys)

def get_element_text(by_locator):
    return driver.find_element(*by_locator).text

def select_dropdown(by_locator,text):
    dropdown = Select(driver.find_element(*by_locator))
    dropdown.select_by_visible_text(text)

def take_screenshot(location):
    driver.save_screenshot(location)