from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser, language):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket") is True, "There is no button adding item to cart"
