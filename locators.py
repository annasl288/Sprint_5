from selenium.webdriver.common.by import By

class MainPage:
    HEADER = (By.XPATH, ".//h1[text() = 'Соберите бургер']") # Заголовок "Соберите бургер"
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка "Личный кабинет"
    BUNS_BUTTON = (By.XPATH, ".//span[text() = 'Булки']") # Кнопка "Булки"
    BUNS_TAB_ACTIVE = (By.XPATH, ".//span[text() = 'Булки']/parent::div[contains(@class, 'tab_tab_type_current')]") # Активный раздел "Булки"
    SAUCES_BUTTON = (By.XPATH, ".//span[text() = 'Соусы']") # Кнопка "Соусы"
    SAUCES_TAB_ACTIVE = (By.XPATH, ".//span[text() = 'Соусы']/parent::div[contains(@class, 'tab_tab_type_current')]")  # Активный раздел "Соусы"
    FILLINGS_BUTTON = (By.XPATH, ".//span[text() = 'Начинки']") # Кнопка "Начинки"
    FILLINGS_TAB_ACTIVE = (By.XPATH, ".//span[text() = 'Начинки']/parent::div[contains(@class, 'tab_tab_type_current')]")  # Активный раздел "Начинки"

class AccountPage:
    ACCOUNT_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']") # Кнопка "Профиль"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']") # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]") # Логотип
    SIGN_OUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']") # Кнопка "Выход"

class AuthorizationPage:
    HEADER = (By.XPATH, ".//h2[text() = 'Вход']") # Заголовок "Вход"
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']") # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']") # Кнопка "Войти"

class RegistrationPage:
    NAME_INPUT = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти"
    ERROR_MESSAGE_INCORRECT_PASSWORD = (By.XPATH, ".//p[text() = 'Некорректный пароль']") # Сообщение о неверном пароле

class RecoverPage:
    LOGIN_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти"