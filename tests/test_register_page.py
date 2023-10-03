import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import REGISTER_PAGE


@pytest.mark.parametrize('xpath', [
    "//*[@name='firstname']", "//*[@name='lastname']", "//*[@id='input-password']",
    "//*[@name='email']", "//*[@name='agree']", '//*/button[contains(@type, "submit")]'],
                         ids=["Input field 'First_name'", "Input field 'Last_name'", "Input field 'Password'",
                              "Input field 'e-mail'", "Checkbox agree 'Privacy Policy'", "Button 'Continue'"])
def test_login_page(browser, xpath):
    browser.get(browser.url + REGISTER_PAGE)
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
