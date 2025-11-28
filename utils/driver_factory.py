import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def load_config():
    config_path = os.path.join(os.getcwd(), "config", "config.json")
    with open(config_path) as f:
        return json.load(f)


def get_driver():
    config = load_config()
    browser = config.get("browser", "chrome")

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--incognito")
        options.add_argument("--disk-cache-size=0")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Raise error for unsupported browsers
    raise ValueError(f"Unsupported browser: {browser}. Please use 'chrome' or add support for other browsers.")
