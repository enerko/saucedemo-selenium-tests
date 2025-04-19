from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import allure

from utils.helper import SeleniumHelper

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(driver)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.helper.fill_input(self.username_field, username)

    def enter_password(self, password):
        self.helper.fill_input(self.password_field, password)
    
    def click_login(self):
        self.helper.click(self.login_button)

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()