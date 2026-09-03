from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

import allure


class CardShop:
    """
    Класс страницы корзины/товаров (CardShop).
    Предоставляет методы для взаимодействия с элементами корзины
    на странице https://www.saucedemo.com/.
    """

    @allure.step("Инициализация страницы корзины и настройка ожидания")
    def __init__(self, driver):
        """
        Инициализирует экземпляр класса CardShop.
        Параметры: driver (selenium.webdriver.remote.webdriver.WebDriver):
        экземпляр драйвера Selenium.
        Возвращаемое значение: None
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    @allure.step("""Переход к оформлению заказа на странице
    InformPage нажатием кнопки Checkout""")
    def checkout(self) -> None:
        """
        Нажимает на кнопку оформления заказа (локатор #checkout).
        Параметры: Нет.
        Возвращаемое значение: None
        """
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#checkout"))
        ).click()
