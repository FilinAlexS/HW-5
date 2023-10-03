import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('xpath', [
    "//*[contains(@name, 'search')]", "//*[@id='logo']//img",
    "//*[@id='header-cart']//button", "//*[contains(@class, 'product-thumb')]",
    "//*[@id='content']/*//*//*//button[1]"],
                         ids=["Input field 'search'", "Check icon 'OpenCart'",
                              "Button 'Cart'", "Items in the 'featured' section", "Button 'Add to cart' on items"])
def test_main_page(browser, xpath):
    browser.get(browser.url)
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))
