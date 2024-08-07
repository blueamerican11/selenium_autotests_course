import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose user language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        if language is not None:
            print("\nstart chrome browser for test..")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)
        else:
            raise pytest.UsageError('--language should be en/ru/fr etc.')
    elif browser_name == "firefox":
        if language is not None:
            print("\nstart firefox browser for test..")
            options = Options()
            options.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(options=options)
        else:
            raise pytest.UsageError('--language should be en/ru/fr etc.')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
