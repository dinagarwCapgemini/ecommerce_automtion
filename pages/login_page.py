from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class LoginPage(BasePage):
    # Locator constants
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, user, pwd):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, pwd)
        self.click(*self.LOGIN_BUTTON)
