from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver


class Total:
    # Инициализация класса
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.price = None

    # Нахождение итоговой суммы
    def total(self):
        total = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")))

        summary = total.get_attribute("textContent").strip()

        price = summary.replace("Total: $", "").strip()
        return price
