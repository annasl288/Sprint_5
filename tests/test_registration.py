from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import RegistrationPage, AuthorizationPage


class TestRegistration:

    def test_registration_success(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegistrationPage.REGISTRATION_BUTTON))

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys('Анна')
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a120@ya.ru')
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys('qwerty')

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(AuthorizationPage.HEADER))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_registration_incorrect_password_message(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegistrationPage.REGISTRATION_BUTTON))

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys('Анна')
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys('annaslobodyanyuk14a120@ya.ru')
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys('123')

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()

        assert driver.find_element(*RegistrationPage.ERROR_MESSAGE_INCORRECT_PASSWORD).text == 'Некорректный пароль'