from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

import allure


class ProfileCalc:
    """
    Класс страницы калькулятора (ProfileCalc).
    Предоставляет методы для взаимодействия с
    элементами калькулятора на странице
    https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
    """

    def __init__(self, driver):
        """
        Инициализирует экземпляр класса ProfileCalc.
        Параметры: driver (selenium.webdriver.remote.webdriver.WebDriver):
        экземпляр драйвера Selenium.
        Возвращаемое значение: None
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java"
            "/slow-calculator.html")
        self.sec = None

    @allure.step("Ввод значения задержки в {sec} в поле #delay")
    def input_delay(self, sec: str | int) -> None:
        """
        Вводит значение задержки в поле ввода (локатор #delay).
        Параметры: sec (int): значение задержки (в секундах),
        которое нужно ввести.
        Возвращаемое значение: None
        """
        self.sec = sec
        input_delay = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#delay")))
        input_delay.clear()
        input_delay.send_keys(str(sec))

    @allure.step("Нажатие на кнопку с цифрой: {num}")
    def input_num(self, num: str | int) -> None:
        """
        Нажимает на кнопку с указанной цифрой на калькуляторе.
        Параметры: num (int | str): цифра
        (или строковое представление цифры), кнопку которой нужно нажать.
        Возвращаемое значение: None
        """
        number = str(num)
        element = (f"//span["
                   f"@class='btn btn-outline-primary' and contains("
                   f"text(), '{number}')]")

        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, element)))
        btn.click()

    @allure.step("Нажатие на оператор: {symbol}")
    def operator(self, symbol: str) -> None:
        """
        Нажимает на кнопку с указанным оператором
        (например, '+', '-', '*', '/').
        Параметры: symbol (str): символ оператора,
        кнопку которого нужно нажать.
        Возвращаемое значение: None
        """
        any_symbol = str(symbol)
        element = f"//span[text()='{any_symbol}']"

        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, element)))
        btn.click()

    @allure.step("Нажатие на кнопку '=' (равно)")
    def equal_press(self) -> None:
        """
        Нажимает на кнопку «равно» (=) на калькуляторе.
        Параметры: Нет.
        Возвращаемое значение: None
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".btn.btn-outline-warning"))
        )
        btn.click()

    @allure.step("Нажатие на кнопку очистки (Clear)")
    def clear(self) -> None:
        """
        Нажимает на кнопку очистки (Clear) на калькуляторе.
        Параметры: Нет.
        Возвращаемое значение: None
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".clear.btn.btn-outline-danger"))
        )
        btn.click()

    @allure.step(
        "Проверка и получение результата на экране: "
        "ожидаемое значение {value}")
    def screen(self, value: str | int) -> str:
        """
        Ожидает появления ожидаемого значения на экране
        калькулятора и возвращает текущее отображаемое значение.
        Параметры: value (int | float | str): ожидаемое
        значение результата, которое должно появиться на экране.
        Возвращаемое значение: str: текстовое значение,
        отображаемое в поле результата (экране) калькулятора.
        """
        wait = self.sec
        waiter = WebDriverWait(self.driver, wait, 1.0)
        display = waiter.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='screen']"))
        )
        waiter.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//div[@class='screen']"), str(value)))
        result_display = display.get_attribute("textContent").strip()
        return result_display
