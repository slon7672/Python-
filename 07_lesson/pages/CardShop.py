from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver


class CardShop:
    # Инициализация класса
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    # Нажатие кнопки checkout
    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#checkout"))
        ).click()
