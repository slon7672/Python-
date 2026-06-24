from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Откройте страницу https://httpbin.org/.
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    sleep(5)

    # Найдите и кликните на ссылку HTML form
    driver.find_element(By.LINK_TEXT, "HTML form").click()

    # Проверьте, что URL изменился на /forms/post.
    current_url = driver.current_url  # свойство — без скобок
    assert current_url == "https://httpbin.org/forms/post"
    print(f"Текущий URL: {current_url}")

    # Вернитесь назад на главную страницу.
    driver.back()

    # Проверьте, что вернулись на исходный URL.
    current_url = driver.current_url  # свойство — без скобок
    assert current_url == "https://httpbin.org/"
    print(f"Текущий URL: {current_url}")

    # Закрываем браузер
    driver.quit()
