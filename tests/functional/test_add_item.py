import csv
import pytest
import os
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage

@pytest.fixture(scope="function")
def setup(driver, username, password):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    yield driver

    # --- Teardown: remove backpack if it's still in cart ---
    try:
        products_page = ProductsPage(driver)
        products_page.remove_backpack_from_cart_button(1)
    except:
        pass  # Already removed or not present

@allure.label("category", "functional")
def test_add_backpack(setup, username):
    allure.dynamic.label("user", username)

    driver = setup
    products_page = ProductsPage(driver)
    
    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == 1, f"Expected 1 item in cart, found {products_page.get_cart_count()}"

@allure.label("category", "functional")
def test_remove_backpack(setup, username):
    allure.dynamic.label("user", username)

    driver = setup
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()
    products_page.remove_backpack_from_cart()

    assert products_page.is_cart_empty(), f"Expected cart to be empty, {products_page.get_cart_count()} still in cart"

@allure.label("category", "functional")
def test_continue_shopping(setup, username):
    allure.dynamic.label("user", username)

    driver = setup
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()
    products_page.click_cart_button()

    assert "Sauce Labs Backpack" in driver.page_source

    cart_page = CartPage(driver)
    cart_page.click_shopping()

    assert "Products" in driver.page_source

@allure.label("category", "functional")
def test_checkout(setup, username):
    allure.dynamic.label("user", username)

    driver = setup
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()
    products_page.click_cart_button()

    assert "Sauce Labs Backpack" in driver.page_source

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    assert "Checkout" in driver.page_source

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.enter_first_name("John")
    checkout_info_page.enter_last_name("Doe")
    checkout_info_page.enter_postal_code("123456")
    checkout_info_page.click_continue()

    assert "Checkout: Overview" in driver.page_source
    assert "Payment Information:" in driver.page_source

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.click_finish()

    assert "Checkout: Complete!" in driver.page_source
