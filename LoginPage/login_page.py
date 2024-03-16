# File: pages/login_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "uname")
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.CSS_SELECTOR, "input[type='submit']")

    def open_page(self, url):
        self.driver.get(url)

    def login_details(self, username, password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

