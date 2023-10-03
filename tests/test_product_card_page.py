import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def go_to_product_card(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, '//*[contains(@class, "image")]/a/img').click()
    yield


@pytest.mark.parametrize('xpath', ['//*[@id="button-cart"]', '//*[contains(@class, "rating")]',
                                   '//*/h1', '//*/form//button[2]', '//*[@id="content"]/ul/li[2]/a'],
                         ids=['Add_to_Card', 'Rating', 'Name_product', 'Button_Compare', 'Link_Specification'])
def test_product_card_page(go_to_product_card, browser, xpath):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
