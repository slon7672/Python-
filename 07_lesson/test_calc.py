import pytest
from pages.profile_calc import ProfileCalc


def test_calc(browser):

    # уникальные значения операторов
    # ('x')
    # ('÷')

    calc = ProfileCalc(browser)

    calc.input_delay("45")
    calc.input_num("7")
    calc.operator("+")
    calc.input_num("8")
    calc.equal_press()

    equal = calc.screen("15")
    res = "15"
    assert equal == res

    browser.quit()
# Открыть страницу калькулятора.
# Ввести значение 45 в поле задержки (локатор #delay).
# Нажать кнопки: 7, +, 8, =.
# Проверить (assert), что в окне отобразится результат 15 через 45 секунд.
