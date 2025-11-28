import os
import pandas as pd
import pytest
import json
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

@pytest.fixture
def driver():
    config = load_config()
    driver = get_driver()
    driver.get(config["base_url"])
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_checkout_flow(driver):
    try:
        login_data = pd.read_csv("data/login_data.csv").iloc[0]
        checkout_data = pd.read_csv("data/checkout_data.csv").iloc[0]

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        confirmation_page = ConfirmationPage(driver)

        # Login
        login_page.login(login_data["username"], login_data["password"])

        # Add items
        inventory_page.add_items_to_cart(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
        inventory_page.go_to_cart()

        # Verify cart
        assert cart_page.verify_items(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
        cart_page.checkout()

        # Checkout
        checkout_page.fill_details(checkout_data["first_name"], checkout_data["last_name"], checkout_data["postal_code"])
        checkout_page.complete_purchase()

        # Confirmation
        assert confirmation_page.verify_message("Thank you for your order!")
        take_screenshot(driver, "confirmation_page")

    except Exception as e:
        take_screenshot(driver, "checkout_flow_failure")
        raise e
