from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


class Price:
    # Инициализация класса
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    # ДВыбор и добавление товаров в корзину
    def add_cart(self, product):
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

    # Переход на страницу корзины
    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".shopping_cart_link"))
        ).click()
