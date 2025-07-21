import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
