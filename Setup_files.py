from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:/Users/shubham_motwani/Downloads/chromedriver_win32 (2)/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
import random

def start_browser():
    driver.get("http://webapp-attack.azurewebsites.net/")
    driver.maximize_window()
    return driver

def generate_random_user_name():
    random_int = random.randint(0, 9999)
    random_name = str(random_int)
    username = "Raj_Sharma"+random_name+"@gmail.com"
    return username
