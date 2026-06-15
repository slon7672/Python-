from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("https://httpbin.org/links/10")
    driver.maximize_window()

    # Ждём загрузки страницы
    sleep(5)

    # Находим все ссылки на странице (тег <a>)
    list_link = driver.find_elements(By.TAG_NAME, "a")

    # Проверяем, что количество ссылок равно 10
    # (ссылок 9, а не 10, потому что текущая страница — это просто текст,
    # а не ссылка)
    assert len(list_link) == 9, f"Найдено ссылок: {len(list_link)}"

    # Проверяем, что все ссылки отображаются на странице
    for x, link in enumerate(list_link, 1):
        assert link.is_displayed(), f"Ссылка номер {x} не отображается"

    # Проверяем, что текст первой ссылки содержит "1"
    # Первая ссылка в списке — это страница "1"
    first_link = list_link[0]
    print(f"Текст первой ссылки: '{first_link.text}'")
    assert "1" in first_link.text, f"Текст первой ссылки: '{first_link.text}'"

    # Закрываем браузер
    driver.quit()
