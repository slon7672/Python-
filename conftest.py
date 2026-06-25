import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# --- Фикстура 1: Сессионная (с окном, куки для gitflic.ru) ---
@pytest.fixture(scope="session")
def session_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzYyZmJiZjctZjRmZi00OTA4LThkNDYtMWY4ZmUyZTY0OGU0",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    yield driver
    driver.quit()


# --- Фикстура 2: Headless для каждого теста (чистый браузер) ---
@pytest.fixture
def driver():
    # Данный код для запуска теста без визуализации в браузере
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # общая часть кода
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


# --- Фикстура 3: для каждого теста (стандартный запуск) ---
@pytest.fixture
def browser():
    # Стандартный запуск теста с открытием окна браузера
    driver = webdriver.Chrome()
    driver.maximize_window()

    # общая часть кода
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
