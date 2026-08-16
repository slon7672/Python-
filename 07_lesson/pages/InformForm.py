from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver


class UserInformForm:
    # Инициализация класса
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Заполнение полей ввода информации пользователя
    def inform(self, first_name, last_name, zip_code):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
        ).send_keys(zip_code)

    # Переход на следующую страницу
    def btn_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#continue"))
        ).click()
