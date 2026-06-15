from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    # Откройте страницу https://httpbin.org/forms/post.
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()
    sleep(5)

    # Найдите поле ввода с названием custname [name="custname"]
    input_name = driver.find_element(By.CSS_SELECTOR, '[name="custname"]')

    # Введите в него ваше имя.
    input_name.send_keys("Ольга")
    sleep(5)

    # Найдите кнопку Submit и нажмите на нее. [//button[text()='Submit order']
    driver.find_element(
        By.XPATH, "//form//button[text()='Submit order']").click()
    sleep(5)

    # Проверьте, что после нажатия URL изменился на https://httpbin.org/post.
    current_url = driver.current_url  # свойство — без скобок
    assert current_url == "https://httpbin.org/post"
    print(f"Текущий URL: {current_url}")

    # Закрываем браузер
    driver.quit()
