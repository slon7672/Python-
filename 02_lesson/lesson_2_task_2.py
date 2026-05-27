def is_year_leap(year) -> bool:
    if year % 4 == 0:
        return True
    else:
        return False


year = int(input("Введите год: "))
x = is_year_leap(year)
print(f"год {year}: {x}")
