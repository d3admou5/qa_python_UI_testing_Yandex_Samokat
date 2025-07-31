import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("-private")

    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
