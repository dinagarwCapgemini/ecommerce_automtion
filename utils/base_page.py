from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_element_located((by, locator))
        )

    def finds(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_all_elements_located((by, locator))
        )

    def click(self, by, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable((by, locator))
        )
        element.click()

    def type(self, by, locator, text, clear_first=True):
        element = self.find(by, locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        return self.find(by, locator).text

    def get_attribute(self, by, locator, attribute):
        return self.find(by, locator).get_attribute(attribute)

    def js_click(self, by, locator):
        element = self.find(by, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, by, locator):
        element = self.find(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_visible(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((by, locator))
        )

    def wait_for_clickable(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable((by, locator))
        )

    def wait_for_invisible(self, by, locator) -> bool:
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                ec.invisibility_of_element_located((by, locator))
            )
        except TimeoutException:
            return False

    def press_tab(self):
        ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def press_enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def press_arrow_down(self):
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

    def hover(self, by, locator):
        element = self.find(by, locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, by, locator):
        element = self.find(by, locator)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, source_by, source_locator, target_by, target_locator):
        source = self.find(source_by, source_locator)
        target = self.find(target_by, target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def select_dropdown_by_text(self, by, locator, text):
        element = self.find(by, locator)
        Select(element).select_by_visible_text(text)

    def switch_to_frame(self, by, locator):
        frame = self.find(by, locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

