import json
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def login(driver, email, password):
    """Use selenium to go to hudl.com, and attempt to login using the given username and password.

    Args:
        driver (selenium.webdriver): an instance of a selenium webdriver that has not yet done anything
        email (str): the email to login with
        password (str): the password to login with

    Returns:
        selenium.webdriver: the selenium webdriver after the login has been attempted
    """
    driver.get("https://www.hudl.com")
    # Find the button to take us to the login page and click it
    button_to_login_page = driver.find_element(
        by=By.CSS_SELECTOR, value='[data-qa-id="login"]'
    )
    button_to_login_page.click()

    # Find the email input box and enter the email
    email_input_box = driver.find_element(
        by=By.CSS_SELECTOR, value='[data-qa-id="email-input"]'
    )
    email_input_box.send_keys(email)
    # Find the password input box and enter the password
    password_input_box = driver.find_element(
        by=By.CSS_SELECTOR, value='[data-qa-id="password-input"]'
    )
    password_input_box.send_keys(password)
    # Find the login button and click it
    login_button = driver.find_element(
        by=By.CSS_SELECTOR, value='[data-qa-id="login-btn"]'
    )
    login_button.click()
    # Sleep for a few seconds to let the page load
    time.sleep(3)

    return driver


def getCredentials(fileName):
    """Read the email and password from the secrets json file

    Args:
        fileName (str): the name of the json file to read from

    Returns:
        tuple: (email, password) where email and password are the values corresponding to the email and password key from the json file
    """
    with open(fileName) as secrets_file:
        login_credentials = json.load(secrets_file)

    email = login_credentials["email"]
    password = login_credentials["password"]
    return (email, password)


class TestHudlLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(executable_path=ChromeDriverManager().install())
        )

    def test_successful_login(self):
        driver = self.driver
        email, password = getCredentials("secrets.json")

        login(driver, email, password)

        # Check if the pages title is "Home - Hudl". You only get redirected to this page on a successful login
        self.assertEqual(driver.title, "Home - Hudl")

    def test_failed_login(self):
        driver = self.driver

        login(driver, "bad_email@blah.com", "password")

        # Check if the login button is disabled, and the title of the page is still "Log In", this will only happen on a failed login
        login_button = driver.find_element(
            by=By.CSS_SELECTOR, value='[data-qa-id="login-btn"]'
        )
        self.assertFalse(login_button.is_enabled())
        self.assertEqual(driver.title, "Log In")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
