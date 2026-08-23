import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# --- Фикстура 1: Сессионная (с окном, куки для gitflic.ru) ---
@pytest.fixture(scope="session")
def session_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://gitflic.ru/")
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "NzYyZmJiZjctZjRmZi00OTA4LThkNDYtMWY4ZmUyZTY0OGU0",
            "domain": "gitflic.ru",
        }
    )
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )
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


@pytest.fixture
def browser_edge():
    # Настройка браузера Edge
    options = webdriver.EdgeOptions()
    options.add_argument("--log-level=3")  # Только критические ошибки
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )  # Убрать DevTools-логи

    driver = webdriver.Edge(options=options)
    driver.maximize_window()  # раскрывает на весь экран
    yield driver
    driver.quit()


@pytest.fixture
def browser_firefox():
    options = FirefoxOptions()
    # options.add_argument("--headless")  # если нужен фоновый режим

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    # driver.set_window_size(1900, 1000)
    driver.maximize_window()  # раскрывает на весь экран

    yield driver
    driver.quit()
