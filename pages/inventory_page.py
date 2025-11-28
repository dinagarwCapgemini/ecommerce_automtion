from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class InventoryPage(BasePage):
    # Locator constants
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_LINK = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        super().__init__(driver)

    def add_items_to_cart(self, items):
        for item in items:
            xpath = f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
            self.click(By.XPATH, xpath)

    def go_to_cart(self):
        self.click(*self.CART_LINK)

    def logout(self):
        self.click(*self.MENU_BUTTON)
        self.wait_for_clickable(*self.LOGOUT_LINK).click()
