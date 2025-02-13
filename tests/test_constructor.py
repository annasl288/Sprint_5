from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPage


class TestConstructor:

    def test_jump_to_buns_success(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPage.SAUCES_BUTTON))
        driver.find_element(*MainPage.SAUCES_BUTTON).click()

        driver.find_element(*MainPage.BUNS_BUTTON).click()

        assert driver.find_element(*MainPage.BUNS_TAB_ACTIVE)


    def test_jump_to_sauces_success(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPage.SAUCES_BUTTON))

        driver.find_element(*MainPage.SAUCES_BUTTON).click()

        assert driver.find_element(*MainPage.SAUCES_TAB_ACTIVE)


    def test_jump_to_fillings_success(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPage.FILLINGS_BUTTON))

        driver.find_element(*MainPage.FILLINGS_BUTTON).click()

        assert driver.find_element(*MainPage.FILLINGS_TAB_ACTIVE)