import pytest
import time
import allure

from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def setup(driver):
    yield driver

def test_login_time(setup, username, password):
    allure.dynamic.label("user", username)

    driver = setup
    login_page = LoginPage(driver)

    start_time = time.time()
    login_page.login(username, password)

    end_time = time.time()
    login_duration = end_time - start_time
    
    max_login_time = 3.0

    assert login_duration <= max_login_time, f"{username} took more than {max_login_time} seconds to log in"

def test_logout_time(setup, username, password):
    allure.dynamic.label("user", username)
    
    driver = setup
    login_page = LoginPage(driver)

    login_page.login(username, password)
    
    products_page = ProductsPage(driver)
    products_page.click_menu()

    start_time = time.time()
    products_page.click_logout()

    end_time = time.time()
    logout_duration = end_time - start_time
    
    max_logout_time = 3.0

    assert logout_duration <= max_logout_time, f"{username} took more than {max_logout_time} seconds to log in"