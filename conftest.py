import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions, ChromeOptions

TEXT_IN_CARD_HEADER = "Please enter your login details."
CATALOG_PAGE = '/index.php?route=product/category&path=20'
ADMIN_PAGE_ON_MY_HOST = '/administration'
ADMIN_PAGE = '/admin'
DEFAULT_URL = 'https://demo.opencart.com'
REGISTER_PAGE = '/index.php?route=account/register'


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default=DEFAULT_URL)


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")

    if browser_name == "firefox":
        service = Service()
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == "chrome":
        service = Service()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError(f'Driver {browser_name} not supported.')

    if maximize:
        driver.maximize_window()

    driver.url = url

    yield driver

    driver.quit()
