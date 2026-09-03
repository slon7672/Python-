from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

import allure


class Total:
    """
    Класс для работы с итоговой суммой в корзине (Total).
    Предоставляет методы для получения значения итоговой стоимости
    на странице https://www.saucedemo.com/.
    """

    @allure.step("Инициализация работы с итоговой суммой")
    def __init__(self, driver):

        """
        Инициализирует экземпляр класса Total.
        Параметры: driver (selenium.webdriver.remote.webdriver.WebDriver):
        экземпляр драйвера Selenium.
        Возвращаемое значение: None
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.price = None

    @allure.step("Получение итоговой суммы заказа")
    def total(self) -> str:

        """
        Находит элемент с итоговой суммой, извлекает текстовое значение,
        очищает его от лишних символов и
        возвращает только числовое значение суммы.
        Параметры: Нет.
        Возвращаемое значение: str: строка с итоговой суммой
        (без префикса «Total: $» и лишних пробелов).
        """

        total = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")))

        summary = total.get_attribute("textContent").strip()

        price = summary.replace("Total: $", "").strip()
        return price
