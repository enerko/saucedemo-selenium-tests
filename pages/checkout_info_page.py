from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import allure

class CheckoutInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        self.helper.fill_input(self.first_name_field, first_name)
    
    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        self.helper.fill_input(self.last_name_field, last_name)

    @allure.step("Enter postal code")
    def enter_postal_code(self, postal_code):
        self.helper.fill_input(self.postal_code_field, postal_code)

    @allure.step("Click continue")
    def click_continue(self):
        self.helper.click(self.continue_button)