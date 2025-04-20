import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.load_credentials import load_credentials_from_csv

@pytest.fixture
def driver():
    chrome_options = Options()

    # For CI
    chrome_options.add_argument("--headless=new")  # Use `--headless=new` for recent Chrome versions
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # Disable automation detection
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Prevent password manager and popups
    chrome_options.add_argument("--incognito")  # or --guest
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 2,
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()

def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames and "password" in metafunc.fixturenames:
        credentials = load_credentials_from_csv()
        metafunc.parametrize("username,password", credentials)


def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames and "password" in metafunc.fixturenames:
        with open("data/credentials.csv", newline="") as csvfile:
            credentials = load_credentials_from_csv()
            ids = [user[0] for user in credentials]
            metafunc.parametrize(("username", "password"), credentials, ids=ids)