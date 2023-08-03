import builtins
# print(dir(builtins))
# print(type(dir(builtins)))
# print(type(builtins))
# builtins_len = len(dir(builtins))
# print(type(builtins_len))
# builtins_list = dir(builtins)
# for i in range(0, builtins_len):
#     if i % 5 == 0:
#         print(builtins_list[i:i+5])

# list = [1,2,3,4,5]
# print(list[0:2])
# for i in range(0, 100):
#     if i % 5 == 0:
#         print(i)


# def degree(x):
#     y = 2
#     def degree_two():
#         return y ** x
#     return degree_two()
# print(degree(4))

# def message(number):
#     def print_message():
#         return 'Число ' + str(number)
#     return print_message()
# print(message(78))

# def message(x):
#     def print_message(y):
#         return x, y
#     return print_message
#
# d = message(4)

# print(d(3))
# print(type(d))
# print(d(8))
# print(d(3))
# print(message(3)(4))


# def message(x):
#     res = [x]
#     def print_message(y=None):
#         if y is None:
#             return res
#         res.append(y)
#         return print_message
#     return print_message
# print(message(10)(11)(12)())


# def main_func():
#     def inner_func():
#         print('Hello my friend')
#     inner_func()
# main_func()

# def main_func1():
#     def inner_func():
#         print('Hello my friend')
#     return inner_func
# a = main_func1()
# # a()
# print(a)  # выдает print из функции, сам print(a()) выдает None почему-то. print(a) печатает  <function main_func1.<locals>.inner_func at 0x0000022B29721120>
#
# def main_func2():
#     name = 'Ivan'
#     def inner_func():
#         print('Hello my friend', name)
#     return inner_func
# d = main_func2()
# d()


# def main_func3(value):
#     def inner_func():
#         print('Hello my friend', value)
#     return inner_func
#
# r = main_func3('Alex')
# r()
# v = main_func3('Misha')
# v()
# y = main_func3('Tosha')
# y()

# def adder(value):
#     def inner(a):
#         return value + a
#     return inner
#
# a2 = adder(2)
# print(a2(7))
#
# a5 = adder(5)
# print(a5(10))

# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return  count
#     return inner
#
# q = counter()
# print(q())
# print(q())
# print(q())
# print(q())


# def avarage_numbers():
#     numbers = []
#     def inner(number):
#         numbers.append(number)
#         print(numbers)
#         return sum(numbers)/len(numbers)
#     return inner
#
# r1 = avarage_numbers()
#
# print(r1(5))
# print(r1(10))
# print(r1(15))
# # результат
# # [5]
# # 5.0
# # [5, 10]
# # 7.5
# # [5, 10, 15]
# # 10.0
# d2 = avarage_numbers()
# print(d2(100))

# def avarage_numbers():
#     summa = 0
#     count = 0
#     def inner(number):
#         nonlocal summa
#         nonlocal count
#         summa += number
#         count += 1
#
#         return summa/count
#     return inner
#
# k = avarage_numbers()
#
# print(k(10))
# print(k(20))
# print(k(50))
# print(k(1000))
# print(avarage_numbers()(10))
# print(avarage_numbers()(50))

from datetime import datetime


# def timer():
#     start = datetime.now()
#
#     def inner():
#         return datetime.now() - start
#     return inner
#
# r = timer()
# print(r())
# print(r())
# print(r())
# r()
# print(r())
#
# from time import perf_counter
#
# def timer():
#     start = perf_counter()
#
#     def inner():
#         return perf_counter() - start
#     return inner
#
# q = timer()
# print(q())
# print(q())
# print(q())
# q()
# print(q())


# def add(a,b):
#     return a + b
#
# def counter(func):
#     count = 0
#     def inner (*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'Функция {func.__name__} вызывалась {count} раз')
#         return func(*args, **kwargs)
#     return inner

# print(counter(add)(10, 30))

# q = counter(add)
# q(10, 20)
# print(q(5,25))
# print(q(5,25))

# def mult(a, b, c):
#     return a * b * c
#
# j = counter(mult)
# print(j(12,3,3))
# print(j(12,3,3))
#
# print(counter(mult)(10, 12, 15))


# замыкание это внутренняя функция, которая возвращается из внешней и использует переменные из внешнего скоупа
# каждое замыкание хранит свое состояние, они не пересекаются.
# хранит состояниеа(данные), предоставляет инструмента для работы с ними, "скрывает" данные, помогает избегать global
#////////////////////////
# def names():
#     all_names = []
#
#     def inner(name: str) -> list:
#         all_names.append(name)
#         return all_names
#
#     return  inner
#
#
# if __name__ == '__main__':
#     boys = names()
#     girls = names()
#     print(boys('Vasya'))  #     print(boys('Petya')) #     print(boys('Dima')) #     print(girls('Lena'))
#     print(girls('Olya'))  #     print(girls('Sveta'))
# #     #////////////////////
#     boys = names()
#     boys('Vasya')
#     boys('Petya')
#     print(boys.__closure__[0].cell_contents)


# def counter():
#     count = 0
#     def inner(value:int) -> int:
#         nonlocal count
#         count += value
#         return count
#     return inner
#
# if __name__ == '__main__':
#     count = counter()
#     print(count(1))      print(count(1))     print(count(1))     print(count(-3))

# def pow_(base):
#     def inner(value):
#         return value ** base
#     return inner

# def pow_(base):
#     return lambda value: value ** base
#
# if __name__ == '__main__':
#     pow__ = pow_(2)
#     pow__2 = pow_(3)
#     print(pow__(2))
#     print(pow__(5))
#     print(pow__(6))
#     print(pow__(7))
#     print(pow__2(5))
#     print(pow__2(6))
#     print(pow__2(7))
#     p = pow_(2)
#     print(p(5))