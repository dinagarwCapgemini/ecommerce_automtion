from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class ConfirmationPage(BasePage):
    # Locator constants
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')

    def __init__(self, driver):
        super().__init__(driver)

    # verify message
    def verify_message(self, message):
        return message in self.get_text(*self.COMPLETE_HEADER)
