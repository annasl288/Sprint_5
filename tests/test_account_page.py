from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPage, AccountPage, AuthorizationPage


class TestAccountPage:

    def test_jump_to_account_page_by_account_button_click_success(self, driver, login):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(AccountPage.ACCOUNT_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


    def test_jump_to_constructor_by_constructor_button_click_success(self, driver, login):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AccountPage.CONSTRUCTOR_BUTTON))

        driver.find_element(*AccountPage.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPage.HEADER))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_jump_to_constructor_by_logo_button_click_success(self, driver, login):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AccountPage.LOGO_BUTTON))

        driver.find_element(*AccountPage.LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPage.HEADER))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_sign_out_success(self, driver, login):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AccountPage.SIGN_OUT_BUTTON))

        driver.find_element(*AccountPage.SIGN_OUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(AuthorizationPage.HEADER))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'