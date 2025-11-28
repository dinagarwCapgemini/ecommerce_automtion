from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class CheckoutPage(BasePage):
    # Locator constants
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    def __init__(self, driver):
        super().__init__(driver)

    # fill details in the form
    def fill_details(self, first_name, last_name, postal_code):
        self.type(*self.FIRST_NAME, first_name)
        self.type(*self.LAST_NAME, last_name)
        self.type(*self.POSTAL_CODE, str(postal_code))
        self.click(*self.CONTINUE_BUTTON)

    # submit purchase
    def complete_purchase(self):
        self.click(*self.FINISH_BUTTON)
