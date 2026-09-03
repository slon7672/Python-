import allure
from pages.AuthorizationPage import Authorization
from pages.CardShopPage import CardShop
from pages.InformPage import UserInformForm
from pages.ProductsListPage import Price
from pages.SummaryPage import Total


@allure.title("Тест: полный сценарий покупки в интернет‑магазине")
@allure.description(
    "Тест проверяет полный сценарий оформления заказа: "
    "авторизация, добавление товаров в корзину, "
    "переход к оформлению, ввод данных пользователя и проверка итоговой суммы."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.NORMAL)
def test_shop(browser_firefox):
    aut = Authorization(browser_firefox)
    cs = CardShop(browser_firefox)
    inf = UserInformForm(browser_firefox)
    prod = Price(browser_firefox)
    summ = Total(browser_firefox)

    with allure.step("Авторизация пользователя: standard_user / secret_sauce"):
        aut.user_name_input("standard_user")
        aut.user_password_input("secret_sauce")
        aut.log_in()

    with allure.step("Добавление товаров в корзину"):
        prod.add_cart("Sauce Labs Backpack")
        prod.add_cart("Sauce Labs Bolt T-Shirt")
        prod.add_cart("Sauce Labs Onesie")
        prod.open_cart()

    with allure.step("Переход к оформлению заказа (Checkout)"):
        cs.checkout()

    with allure.step("Ввод данных пользователя: Иван Иванов, индекс 123456"):
        inf.inform("Иван", "Иванов", "123456")
        inf.btn_continue()

    with (allure.step("Проверка итоговой суммы заказа")):
        actual_summ = summ.total()
        expected_summ = "58.29"
        assert actual_summ == expected_summ, (
            f"Ожидалось '{expected_summ}', "
            f"но на экране '{actual_summ}'"
        )

    browser_firefox.quit()
