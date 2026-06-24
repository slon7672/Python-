from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading(browser):
    wait = WebDriverWait(browser, 10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    browser.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    edit_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div[id='start'] button")
    ))
    edit_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    text = wait.until(EC.presence_of_element_located(
        (By.ID, "finish")
    ))
    # 4. Сделайте скриншот страницы
    browser.save_screenshot("Python-/screenshots/Hello World.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert text.text == "Hello World!"
