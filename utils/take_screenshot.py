import os
from datetime import datetime
import allure

def take_screenshot(driver, filename):
    screenshots_dir = os.path.join(os.getcwd(), "reports", "allure-results")
    os.makedirs(screenshots_dir, exist_ok=True)

    # Clear old screenshots before saving new ones
    for file in os.listdir(screenshots_dir):
        file_path = os.path.join(screenshots_dir, file)
        if os.path.isfile(file_path) and file.endswith(".png"):
            os.remove(file_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(screenshots_dir, f"{filename}_{timestamp}.png")

    driver.save_screenshot(filepath)
    allure.attach.file(filepath, name=filename, attachment_type=allure.attachment_type.PNG)
    print(f"Screenshot saved at: {filepath}")
    return filepath
