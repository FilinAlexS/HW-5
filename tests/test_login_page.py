import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import TEXT_IN_CARD_HEADER, ADMIN_PAGE, ADMIN_PAGE_ON_MY_HOST, DEFAULT_URL


@pytest.mark.parametrize('xpath', [
    "//*[@name='username']", "//*[@id='input-password']",
    "//*[text()='OpenCart']", "//*/button[contains(@type, 'submit')]",
    '//*[contains(@class, "card-header")]'],
                         ids=["Input field 'username'", "Input field 'password'",
                              "Find text 'OpenCart'", "Button 'Login'", "Check text in 'card-header'"])
def test_login_page(browser, xpath):
    if browser.url != DEFAULT_URL:
        browser.get(browser.url + ADMIN_PAGE_ON_MY_HOST)
    else:
        browser.get(browser.url + ADMIN_PAGE)

    if "card-header" in xpath:
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element((By.XPATH, xpath), TEXT_IN_CARD_HEADER))
    else:
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, xpath)))
