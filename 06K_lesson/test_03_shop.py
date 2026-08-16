from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 3) Покупка
# Создавайте файл test_03_shop.py и добавьте в него автотест с шагами:
def test_byu(browser_firefox):
    wait = WebDriverWait(browser_firefox, 10)

    # 1. Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    browser_firefox.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь как пользователь standard_user.
    user_name = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#user-name")))
    user_name.clear()
    user_name.send_keys("standard_user")

    password = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#password")))
    password.clear()
    password.send_keys("secret_sauce")

    login = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#login-button")))
    login.click()

    # 3. Добавьте в корзину товары:
    btn_add_backpack = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
    btn_add_backpack.click()

    btn_add_t_shirt = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
    btn_add_t_shirt.click()

    btn_add_onesie = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")))
    btn_add_onesie.click()

    # 4. Перейдите в корзину.
    shopping_cart = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".shopping_cart_link")))
    shopping_cart.click()

    # 5. Нажмите Checkout.
    checkout = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#checkout")))
    checkout.click()

    # 6. Заполните форму своими данными: имя, фамилия, почтовый индекс.
    first_name = browser_firefox.find_element(
        By.CSS_SELECTOR, "#first-name")
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = browser_firefox.find_element(
        By.CSS_SELECTOR, "#last-name")
    last_name.clear()
    last_name.send_keys("Иванов")

    postal_code = browser_firefox.find_element(
        By.CSS_SELECTOR, "#postal-code")
    postal_code.clear()
    postal_code.send_keys("456789")

    # 7. Нажмите кнопку Continue.
    btn_continue = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#continue")))
    btn_continue.click()

    # 8. Прочитайте со страницы итоговую стоимость (Total).
    total = browser_firefox.find_element(
        By.CSS_SELECTOR, ".summary_total_label")
    summary = total.get_attribute("textContent").strip()

    # 9. Проверьте, что итоговая сумма равна $58.29.
    price = summary.replace("Total: $", "").strip()
    assert price == "58.29", f"Ожидалось '58.29', но на экране '{summary}'"

    # 10. Закройте браузер.
