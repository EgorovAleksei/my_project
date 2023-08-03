
lst = ['Сретенский бульвар', 'Тургеневская', 'Китай-город 2', 'Китай-город 1']
print(str(lst))

# class Chain_sum(int):
#     def __call__(self, value=0):
#         return Chain_sum(self + value)
# print(Chain_sum(5)(10)(25)(5)()())



# p = list(map(int, input().split()))
# d = dict([[x for x in i.split('=')] for i in input().split()])
# d = dict([i.split('=') for i in input().split()])
# x = tuple(map(int, input().split()))

# def transkript(s, sep='-'):
#     return ''.join([t[i] if i in t else i for i in s]).replace(' ', sep)
# s = '1 2 3 4 5 6'
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
#
# def dek1(func):
#     @wraps(func)
#     def wrapper(s):
#         return sum(func(s))
#     return wrapper
#
#
#
# @dek1
# def get_list(s: str):
#     '''Функция для формирования списка целых значений'''
#     return list(map(int, s.split()))
#
#
# print(get_list(s))
#
# print(get_list.__name__)
# print(get_list.__doc__)
#
# pprint.pprint(locals())

# def chain_sum(number):
#     res = number
#     def wrapper (number2=None):
#         nonlocal res
#         if number2 is None:
#             return res
#         res += number2
#         return wrapper
#     return wrapper
#
#
# print(chain_sum(4)(4)())


# d = {word.split(':')[0]: {i.split(': ')[1] for i in lst_in if i.split(":")[0] == word.split(':')[0]} for word in lst_in}


#  [print(*[i]*N) for i in range(N)]  # ОЧЕНЬ ХОРОШЕЕ РЕШЕНИЕ в одну строку с печатью


# print(l[len(l)-1])
# print(l)
# def un(li: list) -> list:
#     li.append(li[len(li)-1]+1)
#     return [li[x] for x in range(len(li)-1) if li[x] != li[x+1]]
#
# print(un(l))


# def un1(arr):
#     f = 0
#     s = 0
#     while s < len(arr):
#         if not (s < len(arr) - 1 and arr[s] == arr[s + 1]):
#             arr[f] = arr[s]
#             f += 1
#         s += 1
#     return arr
#
# print(un1(l))


# s1, s2 = map(str, input().split())
# s1 = 'x00008'
# x1, x2, x3 =  map(str, input().split())

# print(('00' + x1)[:-4:-1])
# print(('00' + x2)[:-4:-1])
# print(('00' + x3)[:-4:-1])
# print(s1[-3::])
# s2 = iter(s1)
# print(next(s2))
#
# print(''.join(reversed(s1)))
# print(reversed(s1))
# new = ''
# for i in s1:
#     new = ''.join(i) + new
# print(new)

# def chain_sum(number):
#     res = number
#     def wrapper (number2=None):
#         nonlocal res
#         if number2 is None:
#             return res
#         res += number2
#         return wrapper
#     return wrapper

# class chain_sum:
#     def __init__(self, number):
#         self._number = number
#
#     def __call__(self, value = 0):
#         return chain_sum(self._number + value)
#
#     def __str__(self):
#         return  str(self._number)

# #
# print(chain_sum(5)(10)(25)(5))
# print(chain_sum(5)(10)(25)(6)())
# print(chain_sum(5)(10)(25)(5)(8)(13)(654)()(1))

#
# class chain_sum(int):
#     def __call__(self, addition = 0):
#         return chain_sum(self + addition)
#
#
#
# print(1 + chain_sum(5)(10)(25)(5))
# print(chain_sum(5)(10)(25)(6)())
# print(chain_sum(5)(10)(25)(5)(8)(13)(654)()(1))


import timeit

"""Рисуем круг"""
# from turtle import *
#
# t = Turtle()
# bgcolor('black')
# t.pencolor('purple')
# t.speed(-100)
#
# for i in range(340):
#     t.circle(190-i, 90)
#     t.left(90)
#     t.circle(190-i, 90)
#     t.left(18)
#     if i > 190:
#         t.pensize(3)
# mainloop()


"""считает время выполнения цикла"""
# value = 100_000_000
# def loop() -> int:
#     return sum(range(value))
# print(f'Loop: {timeit.timeit(loop, number=-1)}')
"""считает время выполнения цикла"""

#
# def get_values() -> list:
#     return [random.randint(0, 9) for _ in range(20)]
#
#
# print(get_values())
#
# user_id, user_photo, user_massege, *values = get_values()
#
# print(user_id)
# print(user_photo)
# print(user_massege)
# print(values)

# a = [2]
# b, = a
# print(b)
# print(type(b))

# def test(x,y):
#     return  x + y
#
# # if __name__ == '__main__':
# #     res = test(1,2)
# #     print(f'test = {res} | __name__: {__name__}')
#
# def main():
#     res = test(1, 2)
#     print(f'test = {res} | __name__: {__name__}')
#
# if __name__ == '__main__':
#     main()


# args = ['start', '-h', 'help', 'dfdf', 1, '-k']
#
# match args:
#     case ['start']:
#          print(f'Добавьте аргументы')
#     case ['start', ('-h' | '--help' | 'help')]:
#         print('Арг')
# case ['start', *arg]:
#     print(f'Все аргументы после старт: {arg}')
# case ['start', _, *arg]:
#     print(f'аргументы пропуская 2 {arg}')
# args1 = ['start', '-h']
# match args1:
#     case ['start']:
#          print(f'Добавьте аргументы')
#     case ['start', ('-h' | '--help' | 'help') as hlp]:
#         print('Если 2 аргумента и 2 из них совпадает с '
#               f'-h -help helg и т.д. и засовывает его в hlp если надо hlp= {hlp}')

# arg_name = ['start', 'Plyuh']
# black_list = ['Plyuh1', 'sdf', 'omnlm,', 'All123']
#
# match arg_name:
#     case ['start', nickname] if nickname not in black_list:
#         print(f'Пользователь: {nickname}')
#     case _:
#         print(f'Пользоватеаль {arg_name[1]} заблокирован')

# class switch:
#     on = 1
#     off = 0
# status = int(input('вв'))
#
# match status:
#     case switch.on:
#         print("Switch is on")
#     case switch.off:
#         print('Switch is off')
#
# def http_status(status: int):
#     match status:
#         case 400:
#             return 'Bad request'
#         case 401:
#             return 'Unauthorizes'
#         case 404:
#             return "Non found"


"""пример использования __name__ == '__main__' """
# username = ''
#
# def choose_username():
#     global username
#     username = input('Введите логин:')
#     if len(username) > 5:
#         print("Ваш логин сохранен.")
#     else:
#         print('Пожалуйста, выберите имя пользователя длиной более пяти символов.')
#         choose_username()
#
# def print_username():
#    print(username)
#
# def main():
#     choose_username()
#     print_username()
#
# if __name__ == '__main__':
#    main()


# замеряем вржемя запроса requests и grequests

# import grequests
# start_time = time.time()

# site = "https://vk.ru"
# for _ in range(100):
#     requests.get(site)
# site = ["https://vk.ru" for x in range(100)]
#
# response = (grequests.)
#
# print('%s seconds ' % (time.time()-start_time))
# print("finish")


# просто райндомайзер который плохо работает.
# import random
# print('Рандомайзер')
# print()
#
# connect = True
#
# while connect:
#     a = int(input('От: '))
# #    a = input('От: ')
#     print()
#     b = int(input('До: '))
# #    b = input('до: ')
#     print()
#     if b < a:
#         print('a должно быть больше b')
#         continue
#     finish= random.randint(int(a),int(b))
#     print('Ответ:', finish)\
#
# # input()
