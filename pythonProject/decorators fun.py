# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper()
# @my_decor
# def my_func():
#     print('Тут основная функция')
#
# # my = my_decor(my_func)
# # my
# my_func

# def my_decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#     return wrapper
# @my_decor
# def my_func(number):
#     return print(number **2)

# my = my_decor(my_func)
# my
# my_func

#my_func(10)

import time

def my_decor(func):
    def my_wr():
        stat_time = time.time()
        func()
        print(time.time() - stat_time)
    return my_wr

@my_decor
def sp():
    spisok = [
        i ** 2
        for i in range(1000000)
        if i % 2 == 0
    ]
    print(spisok)

sp()