import pytest
from string_utils import StringUtils

# “Тест” — не пустая строка.
# “123” — числа как строка.
# “04 апреля 2023” — строка с пробелами.


@pytest.fixture(scope="module")
def sp():
    return StringUtils()


@pytest.mark.pozitive
def test_capitalize_valid(sp):
    assert sp.capitalize("text") == "Text"
    assert sp.capitalize("привет") == "Привет"
    assert sp.capitalize("в") == "В"


@pytest.mark.pozitive
def test_capitalize_empty(sp):
    assert sp.capitalize("") == ""


@pytest.mark.pozitive
def test_capitalize_num(sp):
    res = sp.capitalize("123")
    assert res == "123"
    print(res)  # проверяем, что отображается


@pytest.mark.pozitive
def test_trim_text(sp):
    assert sp.trim(" Строка с пробелом впереди") == "Строка с пробелом впереди"


@pytest.mark.pozitive
def test_trim_space(sp):
    res = sp.trim(" ")
    assert res == ""
    print(res)  # проверяем, что отображается


@pytest.mark.pozitive
def test_contains_true(sp):
    assert sp.contains("Доброе утро!", "б")


@pytest.mark.pozitive
def test_contains_false(sp):
    assert not sp.contains("Доброе утро!", "ю")


@pytest.mark.pozitive
def test_delete_symbol(sp):
    res = sp.delete_symbol("Доборое утро!", "о")
    assert res == "Дбре утр!"
    print(res)


@pytest.mark.positive
def test_delete_symbols_list(sp):
    text = "Доборое утро!"
    symbols_to_delete = ["о", "р"]
    for symbol in symbols_to_delete:
        text = sp.delete_symbol(text, symbol)
        print(text)
    assert text == "Дбе ут!"


# Пустая строка — “”.
# Строка с пробелом — “ ”.
# None.
# Пустой список — [ ] (если метод принимает список).


@pytest.mark.negativ
def test_capitalize_none(sp):
    with pytest.raises(AttributeError):
        sp.capitalize(None)


@pytest.mark.negativ
def test_trim_none(sp):
    with pytest.raises(AttributeError):
        sp.trim(None)


@pytest.mark.negative
def test_contains_not_found(sp):
    result = sp.contains("Доброе утро!", "Б")
    assert result is not True
    assert result is False


@pytest.mark.negative
def test_delete_symbol_empty_list(sp):
    with pytest.raises(TypeError):
        sp.delete_symbol("Доброе утро!", [])
