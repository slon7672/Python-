from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


class Authorization:
    # Инициализация класса, переход на страницу сайта
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com/")

    # Введение логина
    def user_name_input(self, username):
        user_name = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#user-name")))
        user_name.clear()
        user_name.send_keys(username)

    # Введение пароля
    def user_password_input(self, pas):
        password = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#password")))
        password.clear()
        password.send_keys(pas)

    # Нажатие кнопки авторизации
    def log_in(self):
        login = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#login-button")))
        login.click()
