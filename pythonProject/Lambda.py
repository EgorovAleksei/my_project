"""площадь прямоугольника через функцию"""
# def rectangle_area(a,b):
#     return a * b
# print(rectangle_area(17,14))

"""площадь прямоугльника через лямбда функцию"""
# print((lambda a, b : a * b)(17, 14))

""" функция ищет какое число больше из 2"""
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(25,17))

""" функция лямбда ище какое из 2 числел больше"""

print((lambda a,b: a if a > b else b)(25, 14))

rectangle = int(input('Введите сторону квадрата:'))
print((lambda s: s + s + s + s)(rectangle))

print((lambda a, b, c: (a+b+c)/3)(10, 20, 30))
