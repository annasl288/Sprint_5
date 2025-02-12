import pytest
from selenium import webdriver

from locators import MainPage, AuthorizationPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def login(driver):

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*MainPage.LOGIN_BUTTON).click()

    driver.find_element(*AuthorizationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a111@ya.ru')
    driver.find_element(*AuthorizationPage.PASSWORD_INPUT).send_keys('qwerty')
    driver.find_element(*AuthorizationPage.LOGIN_BUTTON).click()

    return driver