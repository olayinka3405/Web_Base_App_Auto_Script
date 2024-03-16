# File: login_page.py

from selenium.webdriver.common.by import By

class LoginPage():


    """
    1. The purpose of a login page is to contain actions common to all page objects
    2. __init__: means initializer and use to initialise a class
    3. self: represent an instant of the class
    4. driver: use to control browser
    """

    def __init__(self, driver):
        self.driver = driver
        # create a variable for every elements locators
        self.username_textbox = (By.ID, "uname")
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.CSS_SELECTOR, "input[type='submit']")

    # create functions for every actions
    def open_page(self, url):
        self.driver.get(url)

    def enter_login_details(self, username, password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

