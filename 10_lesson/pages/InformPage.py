from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

import allure


class UserInformForm:

    """
    Класс страницы формы ввода пользовательских данных (UserInformForm).
    Предоставляет методы для заполнения полей формы и
    перехода к следующему шагу
    на странице https://www.saucedemo.com/.
    """

    @allure.step("Инициализация формы ввода пользовательских данных")
    def __init__(self, driver):

        """
        Инициализирует экземпляр класса UserInformForm.
        Параметры: driver (selenium.webdriver.remote.webdriver.WebDriver):
        экземпляр драйвера Selenium.
        Возвращаемое значение: None
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("""
    Заполнение формы: имя={first_name}, фамилия={last_name}, индекс={zip_code}
    """)
    def inform(self, first_name: str, last_name: str, zip_code: str) -> None:

        """
        Заполняет поля формы: имя, фамилия и почтовый индекс.
        Параметры:
            first_name (str): имя пользователя для ввода в поле #first-name.
            last_name (str): фамилия пользователя для ввода в поле #last-name.
            zip_code (str): почтовый индекс для ввода в поле #postal-code.
        Возвращаемое значение: None
        """

        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
        ).send_keys(zip_code)

    @allure.step("Нажатие кнопки Continue для перехода к SummaryPage")
    def btn_continue(self) -> None:

        """
        Нажимает на кнопку продолжения (локатор #continue).
        Параметры: Нет.
        Возвращаемое значение: None
        """

        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#continue"))
        ).click()
