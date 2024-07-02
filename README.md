## Automation Tests for Login Functionality

This project contains automated tests for the login functionality of a web base application using Selenium and the Page Object Model (POM) design pattern.

### Project Structure
1. Login_Page ('login_page.py')

This class encapsulates the login page actions and elements. It is implemented using the Page Object Model (POM) design pattern to improve the test code's maintainability and readability.

2. Login_Test ('test_login.py')

-This file contains the automated tests for the login functionality. It uses pytest for running tests and WebDriver Manager for managing browser drivers.
-The OpenBrowsers class ensures cross-browser testing by running the same tests across Chrome, Firefox, and Edge browsers.
-The TestLogin class contains the test methods which validate the login functionality with different sets of credentials.
