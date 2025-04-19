from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import allure

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_backpack_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_backpack_from_cart_button = (By.ID, "remove-sauce-labs-backpack")
        self.add_bike_to_cart_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.product_images = (By.CLASS_NAME, "inventory_item_img")
        self.product_title = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Add backpack to cart")
    def add_backpack_to_cart(self, timeout = 10):
        self.helper.click(self.add_backpack_to_cart_button, timeout)

    def add_bike_to_cart(self, timeout = 10):
        self.helper.click(self.add_bike_to_cart_button, timeout)

    @allure.step("Remove backpack from cart")
    def remove_backpack_from_cart(self, timeout = 10):
        self.helper.click(self.remove_backpack_from_cart_button, timeout)
        
    def get_product_images(self):
        return self.helper.find_elements(self.product_images)
    
    def get_product_title(self):
        return self.helper.find_element(self.product_title)