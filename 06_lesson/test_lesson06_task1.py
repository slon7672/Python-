from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # общая часть кода
    driver.implicitly_wait(10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

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
    driver.save_screenshot("screenshots/Hello World.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert text.text == "Hello World!"

    driver.quit()
