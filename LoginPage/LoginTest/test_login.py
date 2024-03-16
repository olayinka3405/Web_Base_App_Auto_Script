# File: test_login.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Web_Base_App_Auto_Script.LoginPage.login_page import LoginPage
from Web_Base_App_Auto_Script.Utilities.test_data import TestData

class OpenBrowsers:

    # running the same tests across different browsers: cross-browser testing.
    @pytest.fixture(scope="function", params=['chrome', 'firefox', 'edge'])
    def initialize_driver(self, request):
        global driver
        if request.param == 'chrome':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif request.param == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif request.param == 'edge':
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        # Set up common configurations for the browser
        driver.implicitly_wait(20)
        driver.maximize_window()

        # Provide the WebDriver instance to the test
        yield driver

        # Teardown: Close the browser after all tests have run
        driver.quit()
@pytest.mark.usefixtures("initialize_driver")
class TestLogin(OpenBrowsers):
    def test_login_valid_credentials(self, initialize_driver):
        driver = initialize_driver
        login_page = LoginPage(driver)

        # Given: The user is on the login page
        login_page.open_page(TestData.url)

        # When: They enter valid credentials
        login_page.enter_login_details(TestData.username, TestData.password)

        # And: Click login button
        login_page.click_login_button()

        # Then: They should be logged in successfully
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
