import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("-private")

    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)
