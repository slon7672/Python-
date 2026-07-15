import pytest
import ast
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser_edge")
class TestUserForm:

    def test_data_types(self, browser_edge):
        wait = WebDriverWait(browser_edge, 10)

        # 1. Откройте страницу:
        # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
        # в Edge или Safari.
        browser_edge.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        # 2. Заполните форму значениями:
        first_name = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='first-name']")))
        first_name.clear()
        first_name.send_keys("Иван")

        last_name = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, " input[name='last-name']")))
        last_name.clear()
        last_name.send_keys("Петров")

        address = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='address']")))
        address.clear()
        address.send_keys("Ленина, 55-3")

        zip_code = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='zip-code']")))
        zip_code.clear()

        city = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='city']")))
        city.clear()
        city.send_keys("Москва")

        country = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='country']")))
        country.clear()
        country.send_keys("Россия")

        e_mail = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='e-mail']")))
        e_mail.clear()
        e_mail.send_keys("test@skypro.com")

        phone = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='phone']")))
        phone.clear()
        phone.send_keys("+7985899998787")

        job_position = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='job-position']")))
        job_position.clear()
        job_position.send_keys("QA")

        company = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='company']")))
        company.clear()
        company.send_keys("SkyPro")

        # 3. Нажмите кнопку Submit.
        submit = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")))
        submit.click()

        WebDriverWait(browser_edge, 10, 0.05)
        ids = browser_edge.find_elements(By.CSS_SELECTOR, '[id]')
        for element in ids:
            print(element.text)
        # Проверьте (assert), что поле Zip code подсвечено красным
        self.check_zip_code_color(ids)
        # Проверьте (assert), что остальные поля подсвечены зеленым
        self.check_all_elements_color(ids)

    @staticmethod
    def check_zip_code_color(ids):
        red = (132, 32, 41, 1)
        green = (15, 81, 50, 1)

        zip_code = ids[3]
        element_id = zip_code.get_attribute("id") or "без ID"
        color = zip_code.value_of_css_property("color")
        actual_rgba = ast.literal_eval(color.replace(
            "rgba", "").strip(" ()"))

        assert actual_rgba in [red, green], \
            (f"Цвет элемента {element_id} ("
             f"{actual_rgba}) не соответствует ни красному, ни зелёному")
        if actual_rgba == green:
            print(f"Элемент {element_id} — цвет поля зелёный")
        elif actual_rgba == red:
            print(f"Элемент {element_id} — цвет поля красный")

    @staticmethod
    def check_all_elements_color(ids):
        red = (132, 32, 41, 1)
        green = (15, 81, 50, 1)

        for index, element in enumerate(ids):
            if index == 3:
                continue
            else:
                element_id = element.get_attribute(
                    "id") or f"элемент_{index}"
                color = element.value_of_css_property("color")
                actual_rgba = ast.literal_eval(color.replace(
                    "rgba", "").strip(" ()"))

                assert actual_rgba in [red, green], \
                    (f"Цвет элемента {element_id} ("
                     f"{actual_rgba}"
                     f") не соответствует ни красному, ни зелёному")
                if actual_rgba == green:
                    print(f"Элемент {element_id} — цвет поля зелёный")
                elif actual_rgba == red:
                    print(f"Элемент {element_id} — цвет поля красный")
