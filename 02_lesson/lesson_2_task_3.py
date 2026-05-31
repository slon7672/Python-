import math


def square(side):
    return math.ceil(side * side)


side = int(input("Введите сторону квадрата: "))
x = square(side)
print(f"Площадь квадрата: {x}")
