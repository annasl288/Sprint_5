from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPage, AuthorizationPage, RegistrationPage, RecoverPage
from urls import URLS


class TestLogin:

    def test_login_from_main_page_by_login_button_click_success(self, driver):

        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPage.LOGIN_BUTTON).click()

        driver.find_element(*AuthorizationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a111@ya.ru')
        driver.find_element(*AuthorizationPage.PASSWORD_INPUT).send_keys('qwerty')
        driver.find_element(*AuthorizationPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPage.HEADER))

        assert driver.current_url == URLS.MAIN_PAGE_URL


    def test_login_from_main_page_by_account_button_click_success(self, driver):

        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        driver.find_element(*AuthorizationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a111@ya.ru')
        driver.find_element(*AuthorizationPage.PASSWORD_INPUT).send_keys('qwerty')
        driver.find_element(*AuthorizationPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPage.HEADER))

        assert driver.current_url == URLS.MAIN_PAGE_URL


    def test_login_from_registration_page_success(self, driver):

        driver.get(URLS.REGISTRATION_PAGE_URL)
        driver.find_element(*RegistrationPage.LOGIN_BUTTON).click()

        driver.find_element(*AuthorizationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a111@ya.ru')
        driver.find_element(*AuthorizationPage.PASSWORD_INPUT).send_keys('qwerty')
        driver.find_element(*AuthorizationPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPage.HEADER))

        assert driver.current_url == URLS.MAIN_PAGE_URL


    def test_login_from_recover_page_success(self, driver):

        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RecoverPage.LOGIN_BUTTON).click()

        driver.find_element(*AuthorizationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a111@ya.ru')
        driver.find_element(*AuthorizationPage.PASSWORD_INPUT).send_keys('qwerty')
        driver.find_element(*AuthorizationPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPage.HEADER))

        assert driver.current_url == URLS.MAIN_PAGE_URL