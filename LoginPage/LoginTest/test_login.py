# File: test_login.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Web_Base_App_Auto_Script.LoginPage.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_valid_credentials(driver):
    login_page = LoginPage(driver)

    # Given: The user is on the login page
    login_page.open_page("https://trytestingthis.netlify.app/")

    # When: They enter valid credentials
    login_page.login_details("test", "test")

    # And: Click login button
    # Then: They should be logged in successfully
    login_page.click_login_button()

    assert "Successful" in driver.page_source



















# # Given: The user is on the login page
# # When: They enter invalid credentials and click login
# # Then: They should see an error message
# def test_login_invalid_credentials(driver):
#     login_page = LoginPage(driver)
#     login_page.open_page("https://example.com/login")
#     login_page.enter_username("invalid_username")
#     login_page.enter_password("invalid_password")
#     login_page.click_login_button()
#     assert "Invalid credentials" in driver.page_source

# # Given: The user is on the login page
# # When: They do not enter any credentials and click login
# # Then: They should see validation messages for both username and password fields
# def test_login_empty_credentials(driver):
#     login_page = LoginPage(driver)
#     login_page.open_page("https://example.com/login")
#     login_page.enter_username("")
#     login_page.enter_password("")
#     login_page.click_login_button()
#     assert "Please enter your username" in driver.page_source
#     assert "Please enter your password" in driver.page_source
#
# # Given: The user is on the login page
# # When: They click on the forgotten password link and provide their username
# # Then: They should see a success message indicating that a reset link has been sent
# def test_forgotten_password(driver):
#     login_page = LoginPage(driver)
#     login_page.open_page("https://example.com/login")
#     login_page.click_forgotten_password_link()
#     login_page.enter_username("username")
#     login_page.click_send_reset_link_button()
#     assert "Password reset link sent successfully" in driver.page_source
#
# # Additional tests can be added here
