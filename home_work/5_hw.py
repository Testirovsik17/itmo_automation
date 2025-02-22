from selenium.webdriver.common.by import By
from selenium import webdriver

def search_elements():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if input and password and submit:
        print ('Элементы найдены')


search_elements()