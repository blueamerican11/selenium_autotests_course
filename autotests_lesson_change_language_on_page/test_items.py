from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_cart_is_present(browser):
    browser.get(link)
    time.sleep(30)
    browser.implicitly_wait(10)

    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed(), \
        "There is no button adding item to cart"