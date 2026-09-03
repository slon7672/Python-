from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

import allure


class Authorization:
    """
    Класс страницы авторизации (Authorization).
    Предоставляет методы для взаимодействия с элементами формы входа
    на странице https://www.saucedemo.com/.
    """

    @allure.step("Инициализация страницы авторизации и переход на сайт")
    def __init__(self, driver):

        """
        Инициализирует экземпляр класса Authorization.
        Параметры: driver (selenium.webdriver.remote.webdriver.WebDriver):
        экземпляр драйвера Selenium.
        Возвращаемое значение: None
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод логина: {username}")
    def user_name_input(self, username: str) -> None:

        """
        Вводит логин в поле ввода (локатор #user-name).
        Параметры: username (str): значение логина для ввода.
        Возвращаемое значение: None
        """

        user_name = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#user-name")))
        user_name.clear()
        user_name.send_keys(username)

    @allure.step("Ввод пароля: {pas}")
    def user_password_input(self, pas: str) -> None:

        """
        Вводит пароль в поле ввода (локатор #password).
        Параметры: pas (str): значение пароля для ввода.
        Возвращаемое значение: None
        """

        password = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#password")))
        password.clear()
        password.send_keys(pas)

    @allure.step("Нажатие кнопки авторизации и перехода к ProductsList")
    def log_in(self) -> None:

        """
        Нажимает на кнопку входа (локатор #login-button).
        Параметры: Нет.
        Возвращаемое значение: None
        """

        login = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#login-button")))
        login.click()
