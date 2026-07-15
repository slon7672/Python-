from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создайте файл test_02_calc.py и добавьте в него автотест с шагами:
def test_calc(browser):
    wait = WebDriverWait(browser, 60)

    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    # в Google Chrome.
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # В поле ввода по локатору #delay введите значение 45.
    input_delay = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#delay")))
    input_delay.clear()
    input_delay.send_keys("45")

    # Предварительная очистка поля ответа
    button_c = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='clear btn btn-outline-danger']")))
    button_c.click()

    # Нажмите на кнопки: 7 + 8 =
    button_7 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='7']")))
    button_7.click()

    button_sum = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='+']")))
    button_sum.click()

    button_8 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='8']")))
    button_8.click()

    # Проверка, что в поле ответа отображаются введенные данные
    screen = browser.find_element(By.CSS_SELECTOR, ".screen")
    formula = screen.get_attribute("textContent").strip()
    assert formula == "7+8", f"Ожидалось '7+8', но на экране '{formula}'"

    # Нажмите на кнопки: =
    button_equal = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='=']")))
    button_equal.click()

    # Проверка, что в окне отобразится результат 15 через 45 секунд.  .screen
    try:
        wait.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, ".screen"), "15"))
        result_screen = browser.find_element(By.CSS_SELECTOR, ".screen")
        result = result_screen.get_attribute("textContent").strip()
        assert result == "15", f"Ожидалось '15', но на экране '{result}'"
    except TimeoutException:
        print("Ошибка: время ожидания истекло, результат 15 не появился")
        raise
