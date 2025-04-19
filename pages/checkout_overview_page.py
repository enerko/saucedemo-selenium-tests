from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import allure

class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.finish_button = (By.ID, "finish")

    @allure.step("Complete checkout")
    def click_finish(self):
        self.helper.click(self.finish_button)