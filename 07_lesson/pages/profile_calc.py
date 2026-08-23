from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver


class ProfileCalc:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        URL = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/"
            "slow-calculator.html"
            )
        self.driver.get(URL)
        self.sec = None

    def input_delay(self, sec):
        self.sec = sec
        input_delay = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#delay")))
        input_delay.clear()
        input_delay.send_keys(str(sec))

    def input_num(self, num):
        number = str(num)
        element = (f"//span["
                   f"@class='btn btn-outline-primary' and contains("
                   f"text(), '{number}')]")

        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, element)))
        btn.click()

    def operator(self, symbol):
        any_symbol = str(symbol)
        element = f"//span[text()='{any_symbol}']"

        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, element)))
        btn.click()

    def equal_press(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".btn.btn-outline-warning"))
        )
        btn.click()

    def clear(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".clear.btn.btn-outline-danger"))
        )
        btn.click()

    def screen(self, value):
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
