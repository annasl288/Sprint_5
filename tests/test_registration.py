from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import RegistrationPage, AuthorizationPage
from urls import URLS
from data import RandomPerson


class TestRegistration:

    def test_registration_success(self, driver):

        driver.get(URLS.REGISTRATION_PAGE_URL)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegistrationPage.REGISTRATION_BUTTON))

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(RandomPerson.NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(RandomPerson.EMAIL)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(RandomPerson.PASSWORD)

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(AuthorizationPage.HEADER))

        assert driver.current_url == URLS.AUTHORIZATION_PAGE_URL


    def test_registration_incorrect_password_message(self, driver):

        driver.get(URLS.REGISTRATION_PAGE_URL)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegistrationPage.REGISTRATION_BUTTON))

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(RandomPerson.NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(RandomPerson.EMAIL)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys('123')

        driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()

        assert driver.find_element(*RegistrationPage.ERROR_MESSAGE_INCORRECT_PASSWORD).text == 'Некорректный пароль'