from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import allure

from utils.helper import SeleniumHelper

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(driver)

        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def click_menu(self):
        """Opens the sidebar menu."""
        self.helper.click(self.menu_button)

    @allure.step("Logout")
    def click_logout(self):
        """Clicks logout button (only works if menu is open)."""
        self.helper.click(self.logout_button)

    def get_cart_count(self):
        """Returns the number of items in the cart (cannot be 0)."""
        badge = self.helper.find_elements(self.cart_badge)
        return int(badge[0].text)

    def is_cart_empty(self, timeout=10):
        """
        Wait until the cart is empty (badge is not present).
        Returns True if the cart is empty within the timeout, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: len(driver.find_elements(*self.cart_badge)) == 0
            )
            return True
        except TimeoutException:
            return False


    @allure.step("Go to cart")
    def click_cart_button(self):
        self.helper.click(self.cart_button)
