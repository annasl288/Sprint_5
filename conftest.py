import pytest
from selenium import webdriver

from locators import MainPage, AuthorizationPage
from urls import URLS
from data import Person

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):

    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPage.LOGIN_BUTTON).click()

    driver.find_element(*AuthorizationPage.EMAIL_INPUT).send_keys(Person.EMAIL)
    driver.find_element(*AuthorizationPage.PASSWORD_INPUT).send_keys(Person.PASSWORD)
    driver.find_element(*AuthorizationPage.LOGIN_BUTTON).click()

    return driver