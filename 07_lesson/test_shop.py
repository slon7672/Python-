import pytest
from pages.Authorization import Authorization
from pages.CardShop import CardShop
from pages.InformForm import UserInformForm
from pages.ProductsList import Price
from pages.SummaryPage import Total


def test_shop(browser_firefox):

    aut = Authorization(browser_firefox)
    cs = CardShop(browser_firefox)
    inf = UserInformForm(browser_firefox)
    prod = Price(browser_firefox)
    summ = Total(browser_firefox)

    aut.user_name_input("standard_user")
    aut.user_password_input("secret_sauce")
    aut.log_in()

    prod.add_cart("Sauce Labs Backpack")
    prod.add_cart("Sauce Labs Bolt T-Shirt")
    prod.add_cart("Sauce Labs Onesie")
    prod.open_cart()

    cs.checkout()

    inf.inform("Иван", "Иванов", "123456")
    inf.btn_continue()

    actual_summ = summ.total()
    assert actual_summ == "58.29", f"Ожидалось '58.29', но на экране '{
        actual_summ}'"

    browser_firefox.quit()
