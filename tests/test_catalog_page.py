import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import CATALOG_PAGE


@pytest.mark.parametrize('xpath', [
    "//*[@id='input-sort']", "//*[contains(@class, 'fa-home')]",
    "//*[@id='button-list']"],
                         ids=["Input field 'Sort By'", "Icon 'Home'",
                              "Search for a 'list' button"])
def test_visibility_of_element(browser, xpath):
    browser.get(browser.url + CATALOG_PAGE)
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))


@pytest.mark.parametrize('xpath, value',
                         [("//*[@id='content']/div[5]/*//li[2]/a", "2"),
                          ("//*[@id='column-left']//a[9]", "Cameras")],
                         ids=["Search and check the element 'pg. 2'", "Search and check in the left menu 'Cameras'"])
def test_text_in_element(browser, xpath, value):
    browser.get(browser.url + CATALOG_PAGE)
    WebDriverWait(browser, 3).until((EC.text_to_be_present_in_element((By.XPATH, xpath), text_=value)))
