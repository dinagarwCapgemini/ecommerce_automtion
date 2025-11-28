
import unittest
import pandas as pd
import json
import os
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
from utils.take_screenshot import take_screenshot
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

def load_config():
    config_path = os.path.join(os.getcwd(), "config", "config.json")
    with open(config_path) as f:
        return json.load(f)

class TestCheckoutFlow(unittest.TestCase):
    def setUp(self):
        config = load_config()
        self.driver = get_driver()
        self.driver.get(config["base_url"])

    def test_checkout_flow(self):
        try:
            login_data = pd.read_csv("data/login_data.csv").iloc[0]
            checkout_data = pd.read_csv("data/checkout_data.csv").iloc[0]

            login_page = LoginPage(self.driver)
            inventory_page = InventoryPage(self.driver)
            cart_page = CartPage(self.driver)
            checkout_page = CheckoutPage(self.driver)
            confirmation_page = ConfirmationPage(self.driver)

            # Login
            login_page.login(login_data["username"], login_data["password"])

            # Add items
            inventory_page.add_items_to_cart(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
            inventory_page.go_to_cart()

            # Verify cart
            self.assertTrue(cart_page.verify_items(["Sauce Labs Backpack", "Sauce Labs Bike Light"]))
            cart_page.checkout()

            # Checkout
            checkout_page.fill_details(checkout_data["first_name"], checkout_data["last_name"], checkout_data["postal_code"])
            checkout_page.complete_purchase()

            # Confirmation
            self.assertTrue(confirmation_page.verify_message("Thank you for your order!"))
            take_screenshot(self.driver, "confirmation_page")
            # Logout
            inventory_page.logout()
            self.assertTrue(self.driver.find_element(By.ID, "login-button").is_displayed())

        except Exception as e:
            take_screenshot(self.driver, "checkout_flow_failure")
            raise e

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
