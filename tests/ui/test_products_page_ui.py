import pytest

from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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

def test_ui_elements(setup):
    driver = setup

    products_page = ProductsPage(driver)

    assert driver.find_element(*products_page.cart_button).is_displayed(), f"Cart icon is missing"
    assert driver.find_element(*products_page.menu_button).is_displayed(), f"Menu button is missing"


def test_images(setup):
    driver = setup

    products_page = ProductsPage(driver)

    for img in products_page.get_product_images():
        assert img.get_attribute("src") != "", f"Broken image detected"

def test_responsive_layout(setup):
    driver = setup

    products_page = ProductsPage(driver)

    # Set window to small size (mobile view)
    driver.set_window_size(375, 812)  # iPhone X size
    assert driver.find_element(*products_page.menu_button).is_displayed(), f"Menu button missing in mobile view"
    
    # Set window back to desktop size
    driver.set_window_size(1280, 800)
    assert driver.find_element(*products_page.cart_button).is_displayed(), f"Cart icon missing in desktop view"

def test_text_style(setup):
    driver = setup

    products_page = ProductsPage(driver)

    product_title = products_page.get_product_title()
    assert product_title.value_of_css_property("font-size") == "20px", f"Incorrect font size"
