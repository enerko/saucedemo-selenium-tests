from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")
        self.shopping_button = (By.ID, "continue-shopping")

    def click_checkout(self):
        self.helper.click(self.checkout_button)
    
    def click_shopping(self):
        self.helper.click(self.shopping_button)