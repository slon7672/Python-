import allure
from pages.profile_calc_page import ProfileCalc


@allure.title(
        "Тест: проверка работы калькулятора с задержкой и операции сложения")
@allure.description("""
Тест проверяет корректность выполнения операции сложения (7 + 8)
на калькуляторе при заданной задержке 45 секунд. Ожидается результат 15.
""")
@allure.feature("Калькулятор с задержкой выполнения операций")
@allure.severity(allure.severity_level.NORMAL)
def test_calc(browser):
    calc = ProfileCalc(browser)

    calc.input_delay("45")
    calc.input_num("7")
    calc.operator("+")
    calc.input_num("8")
    calc.equal_press()

    with allure.step("""
    Проверка, что в окне отобразится результат 15 через 45 секунд
    """):
        equal = calc.screen("15")
        res = "15"
        assert equal == res

    browser.quit()
