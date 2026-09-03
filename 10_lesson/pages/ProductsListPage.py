from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC

import allure


class Price:
    """
    Класс для добавления товаров в корзину (Price).
    Предоставляет методы для добавления товара в корзину и открытия корзины
    на странице https://www.saucedemo.com/.
    """

    @allure.step("Инициализация работы с товарами и настройка ожидания")
    def __init__(self, driver):
        """
        Инициализирует экземпляр класса Price.
        Параметры: driver (selenium.webdriver.remote.webdriver.WebDriver):
        экземпляр драйвера Selenium.
        Возвращаемое значение: None
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    @allure.step("Добавление товара в корзину: {product}")
    def add_cart(self, product: str) -> None:
        """
        Добавляет указанный товар в корзину,
        используя соответствующий локатор по имени.
        Параметры:
            product (str): название товара
            (точное совпадение с ключом в словаре list_products),
            который нужно добавить в корзину.
        Возвращаемое значение: None
        Примечание:
            Если переданный продукт не найден в словаре,
            выводится сообщение в консоль,
            действие по добавлению в корзину не выполняется.
        """
        list_products = {
            'Sauce Labs Backpack':
                'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt':
                'add-to-cart-sauce-labs-bolt-t-shirt',
            'Sauce Labs Onesie':
                'add-to-cart-sauce-labs-onesie',
            'Sauce Labs Bike Light':
                'add-to-cart-sauce-labs-bike-light',
            'Sauce Labs Fleece Jacket':
                'add-to-cart-sauce-labs-fleece-jacket',
            'Test.allTheThings() T-Shirt (Red)':
                'add-to-cart-test.allthethings()-t-shirt-(red)'
        }

        if product in list_products:
            self.wait.until(
                EC.element_to_be_clickable((
                    By.NAME, list_products[product]))
            ).click()
        else:
            print(f"{product} is not a known product")

    @allure.step("Открытие корзины покупок (переход на страницу CardShopPage)")
    def open_cart(self) -> None:
        """
        Нажимает на ссылку для перехода в корзину
        (локатор .shopping_cart_link).
        Параметры: Нет.
        Возвращаемое значение: None
        """
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".shopping_cart_link"))
        ).click()
