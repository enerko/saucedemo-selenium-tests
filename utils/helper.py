from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            self.driver.find_element(*locator).click()
        except Exception as e:
            raise AssertionError(f"Failed to click {locator} button: {repr(e)}")


    def find_element(self, locator, timeout = 10):
        """Waits until finding element and throws a TimeoutException if not found."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout = 10):
        """Waits until finding elements and throws a TimeoutException if not found."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def fill_input(self, locator, value):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)