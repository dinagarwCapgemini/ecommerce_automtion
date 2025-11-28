from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class CartPage(BasePage):
    # Locator constants
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def __init__(self, driver):
        super().__init__(driver)

    # verify items added in the cart
    def verify_items(self, items):
        cart_items = [el.text for el in self.finds(*self.INVENTORY_ITEM_NAME)]
        return all(item in cart_items for item in items)

    def checkout(self):
        self.click(*self.CHECKOUT_BUTTON)
