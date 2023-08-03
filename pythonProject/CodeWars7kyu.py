"""Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
Вычислите сумму чисел в n-й строке этого треугольника (начиная с индекса 1), например: (Ввод -> Вывод)"""

# n ряд это n * (n-1) +1


# def row_sum_odd_numbers(n):
    # sum_n = n * (n - 1) + 1
    # result = sum_n
    # for i in range(n-1):
    #     sum_n = sum_n + 2
    #     result = result + sum_n
    # return result
    # return n ** 3
    # return sum(range(n * (n - 1) + 1, n * (n + 1), 2))
    # sum([_ for _ in range(n * (n - 1), n * (n - 1) + (n * 2)) if _ % 2])
    # sum([i for i in range(sum([i for i in range(1, n+1)])*2) if i % 2][:-n-1:-1])

# print(row_sum_odd_numbers(4))

"""Сумма первого n-го члена ряда Ваша задача - написать функцию, которая возвращает сумму следующих рядов
до n-го члена (параметра).  Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Правила: Вам нужно округлить ответ до 2 знаков после запятой и вернуть его в виде строки.
Если заданное значение равно 0, то оно должно возвращать 0.00
В качестве аргументов вам будут даны только натуральные числа.
Examples:(Input --> Output)
1 --> 1 --> "1.00"   2 --> 1 + 1/4 --> "1.25"  5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57" """

# def series_sum(n):
#     sum = 0
#     delitel = 1
#     for i in range(1, n+1):
#         sum = sum + 1/delitel
#         delitel += 3
#         print(f'{sum:.2f}')
#
#     return '{:.2f}'.format(sum(1.0 / (3 * i + 1) for i in range(n)))
#     return f'{sum(1 / d for d in range(1, n * 3, 3)):.2f}'
#
# print(series_sum(1))



"""Завершите решение так, чтобы оно возвращало значение true, если переданный первый аргумент (строка)
заканчивается 2-м аргументом (также строкой). Examples: solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false """

# string = 'abcde'
# ending = 'cde'
# s_len = len(string)
# e_len = len(ending)
# print(string[-1:])
# # def solution(string, ending):
#     return string[s_len - e_len:s_len] == ending or not ending
#     return string.endswith(ending)
#     return ending in string[-len(ending):]

"""Напишите функцию, которая принимает целое число n и строки в качестве параметров и возвращает строку
из s, повторяющуюся ровно n раз.  6, "I"     -> "IIIIII"  5, "Hello" -> "HelloHelloHelloHelloHello" """

# def repeat_str(repeat, string):
#     return string*repeat
#
# print(repeat_str(4, 'a'))

"""описание: Реализуйте функцию, которая принимает 3 целых значения a, b, c.
Функция должна возвращать значение true, если треугольник может быть построен со сторонами заданной длины,
и значение false в любом другом случае.
(В этом случае все треугольники должны иметь поверхность больше 0, чтобы быть принятыми)."""
# a = 0
# b = 1
# c = 2
# if a and b and c > 0:
#     print(True)
# else:
#     print(False)
#
# def is_triangle(a, b, c):
#     return a and b and c > 0 and a + b > c and a + c > b and b + c > a


"""Часы показывают h часов, m минут и s секунд после полуночи.
Ваша задача - написать функцию, которая возвращает время с полуночи в миллисекундах.
Example: h = 0 m = 1 s = 1  result = 61000"""
# def past(h, m, s):
#     return (h*60*60 + m*60 + s)*1000
#     return timedelta(hours=h, minutes=m, seconds=s) // timedelta(milliseconds=1)



"""Создайте программу, которая фильтрует список строк и возвращает список, в котором есть только имя вашего друга.
Если в имени ровно 4 буквы, вы можете быть уверены, что это должен быть ваш друг! В противном случае, вы можете
быть уверены, что это не так...
Пример: Ввод = ["Райан", "Киран", "Джейсон", "Ты"], Вывод = ["Райан", "Ты"]"""

# x = ["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]
#
# print(x)
# x_new = []
# for i in range(0, len(x)):
#     # print('i=', i)
#     # print('lenX= ', len(x))
#     if len(x[i]) == 4:
#          x_new.append(x[i])
#
# print(x_new)
# x_new2 = []
#
# for y in x:
#     if len(y) == 4:
#         x_new2.append(y)
# print(x_new2)
#
# x_new3 = []
# print( x_new3.append(for z in x if len(z) == 4 ))  #не работает эта форма
# return [f for f in x if len(f) == 4] # достаточно было так
# return filter(lambda name: len(name) == 4, x)
#
# print(x_new3)
# y for y in arr if y < 0

"""Проверьте, содержит ли строка одинаковое количество "x" и "o". Метод должен возвращать логическое
значение и быть нечувствительным к регистру. Строка может содержать любой символ.
Примеры ввода/вывода:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""
# s = 'xxxoooOX'
# s = s.lower()
#
# sX = s.count('x')
# sO = s.count('o')
# print('sX =', sX, "\n", 'sO =', sO)
# print(f'sX= {sX} \nsO= {sO}')
#
# def xo(s):
#     # s = s.lower()
#     # return s.count('x') == s.count('o')
#     return s.lower().count('x') == s.lower().count('o')
# print(xo(s))




"""В этом небольшом задании вам дается строка чисел, разделенных пробелами, и вы должны вернуть самое
 высокое и самое низкое число.
Примеры
high_and_low("1 2 3 4 5") # вернуть "5 1"
высоко_и_лоу("1 2 -3 4 5") # возврат "5 -3"
высоко_и_лоу("1 9 3 4 -5") # возврат "9 -5"
Записи
Все номера действительны в Int32, нет необходимости их проверять.
Во входной строке всегда будет хотя бы одно число.
Выходная строка должна состоять из двух чисел, разделенных одним пробелом, причем наибольшее число должно быть первым."""

# numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4 -55"
# def high_and_low(numbers):
    # list_numbers = numbers.split(' ')
    # numbers_int = list(map(int, list_numbers))
     #result = f'{max(numbers_int)} {min(numbers_int)}'
    # # result = str(max(numbers_int)) + ' ' + str(min(numbers_int))
    # return result
    #
    # nn = [int(s) for s in numbers.split(" ")]
    # return "%i %i" % (max(nn), min(nn))
    #
    # nums = sorted(numbers.split(), key=int)
    # return '{} {}'.format(nums[-1], nums[0])

#     numbers = [int(c) for c in numbers.split(' ')]
#     print(numbers)
#     return f"{max(numbers)} {min(numbers)}"
#
#     return " ".join(x(numbers.split(), key=int) for x in (max, min))
# print(high_and_low(numbers))



"""Примечание: Это ката вдохновлено преобразованием числа в строку!. Попробуй и это тоже.
Описание  Нам нужна функция, которая может преобразовать строку в число. Какие способы достижения этого вы знаете?
Примечание: Не волнуйтесь, все входные данные будут строками, и каждая строка является абсолютно корректным
представлением целого числа."""

# def string_to_number(s):
#     return int(s)



"""Создайте функцию, которая принимает целое число в качестве аргумента и возвращает значение
"Even" для четных или "Odd"нечетных чисел."""
#-----------------------------------------------------------------------------
# def even_or_odd(number):
#     return 'Even' if number % 2 == 0 else 'Odd'
#     return 'Odd' if number % 2 else 'Even'
#     return ["Even", "Odd"][number % 2]
#
#
# print(even_or_odd(5))
#-------------------------------------------------------------------------


"""Тролли атакуют ваш раздел комментариев!
Обычный способ справиться с этой ситуацией - удалить все гласные из комментариев троллей, нейтрализуя угрозу.
Ваша задача - написать функцию, которая принимает строку и возвращает новую строку с удаленными всеми гласными.
Например, строка "Этот веб-сайт для неудачников, ЛОЛ!" станет "Ths wbst s fr lsrs LL!".
Примечание: для этого ката y не считается гласной."""

# s = "This website is for losers LOL!"
#
# def disemvowel(string_):
#     vowel = set('aeiouAEIOU')
#     result = ''
#     for letter in string_:
#         if letter in vowel:     # if not letter in string_   можно без else
#             result = result    #      result += letter
#         else:
#             result = result + letter
#     return result
#
#     return "".join(c for c in string if c.lower() not in "aeiou")
#
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#
# import re
# def disemvowel(string):
#     return re.sub(r"[aeiouAEIOU]", "", string)
# print(disemvowel(s))




"""Учитывая массив единиц и нулей, преобразуйте эквивалентное двоичное значение в целое число.

Например: [0, 0, 0, 1] обрабатывается как 0001, который является двоичным представлением 1.
Примеры:
Тестирование: [0, 0, 0, 1] ==> 1  Тестирование: [0, 0, 1, 0] ==> 2  Тестирование: [0, 1, 0, 1] ==> 5
Тестирование: [1, 0, 0, 1] ==> 9  Тестирование: [0, 0, 1, 0] ==> 2  Тестирование: [0, 1, 1, 0] ==> 6
Тестирование: [1, 1, 1, 1] ==> 15  Тестирование: [1, 0, 1, 1] ==> 11
Однако массивы могут иметь различную длину, а не ограничиваться только 4."""

# def binary_array_to_number(arr):
# #  return int("".join(map(str, arr)), 2)
#
# """ как делаются двоичные числа"""
#     s = 0
#     for digit in arr:
#         s = s * 2 + digit
#         print('S=', s, 'digit= ', digit)
#     return s
#
# arr = [1, 1, 0, 1]
#
# print(binary_array_to_number(arr))

"""Дан массив целых чисел.
Возвращает массив, где первый элемент - это количество положительных чисел, а второй элемент - сумма отрицательных
чисел. 0 не является ни положительным, ни отрицательным.
Если входные данные представляют собой пустой массив или имеют значение null, верните пустой массив.
Пример
Для ввода [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], вы должны вернуться [10, -65]."""

# arr = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
#arr = [1,2,-2,-1]

# def count_positives_sum_negatives(arr):
    # if arr:    # if not arr
    #     count = 0
    #     count_negative = 0    # count, count_negative = 0
    #     for i in arr:
    #         if i <= 0:
    #             count_negative = count_negative + i
    #         else:
    #             count += 1
    #     return [count, count_negative]
    # else:
    #     return []


    # pos = sum(1 for x in arr if x > 0)
    # pos = sum(x>0 for x in arr)
    # neg = sum(x for x in arr if x < 0)
    # return [pos, neg] if len(arr) else []

    # return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

    # return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []


    # output = []
    # if arr:
    #     output.append(sum([1 for x in arr if x > 0]))
    #     output.append(sum([x for x in arr if x < 0]))
    # return output

    # return [] if len(arr) == 0 else [len([i for i in arr if i > 0]), sum([x for x in arr if x < 0])]

# from functools import reduce
# def count_positives_sum_negatives(arr):
#     return arr and reduce(lambda x, y: [x[0] + (y > 0), x[1] + y * (y < 0)], arr, [0, 0])

    # return [
    #     len([n for n in a if n>0]),
    #     sum([n for n in a if n<0])
    # ] if a else []

# print(count_positives_sum_negatives(arr))
# print(sum(arr))

"""На фабрике принтер печатает этикетки для коробок. Для одного вида коробок принтер должен использовать цвета,
которые для простоты обозначаются буквами от а до м.
Цвета, используемые принтером, записываются в управляющую строку. Например, "хорошей" управляющей строкой будет
aaabbbbhaijjjm, что означает, что принтер использовал три раза цвет a, четыре раза цвет b, один раз цвет h,
затем один раз цвет a...
Иногда возникают проблемы: отсутствие цветов, техническая неисправность и выдается "плохая" управляющая строка,
например, aaaxbbbbyyhwawiwjjjwwm с буквами не от a до m.
Вы должны написать функцию printer_error, которая, учитывая строку, вернет частоту ошибок принтера в виде строки,
представляющей рациональное число, числителем которого является количество ошибок, а знаменателем -
длина управляющей строки. Не сводите эту дробь к более простому выражению.
Строка имеет длину, большую или равную единице, и содержит только буквы от a до z."""

# s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# def printer_error(s):
    # count = 0
    # for i in s:
    #     if i > 'm':
    #         count += 1
    # return f'{count}/{len(s)}'
#    return '{}/{}'.format(sum(color > 'm' for color in s), len(s))
#    return f'{sum(i > "m" for i in s)}/{len(s)} '
#     import re
#     return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))


# print(printer_error(s))


"""По городу ходит автобус, и он забирает и высаживает несколько человек на каждой автобусной остановке.
Вам предоставляется список (или массив) пар целых чисел. Элементы каждой пары представляют количество людей,
садящихся в автобус (первый элемент), и количество людей, выходящих из автобуса (второй элемент) на автобусной
 остановке.
Ваша задача - вернуть количество людей, которые все еще находятся в автобусе после последней автобусной станции
(после последнего массива). Несмотря на то, что это последняя автобусная остановка, автобус не пуст, и некоторые
люди все еще в автобусе, и они, вероятно, спят там : D
Взгляните на тестовые примеры.
Пожалуйста, имейте в виду, что тестовые примеры гарантируют, что количество людей в автобусе всегда >= 0.
Таким образом, возвращаемое целое число не может быть отрицательным.
Второе значение в первом целочисленном массиве равно 0, так как автобус пуст на первой автобусной остановке."""


#def number(bus_stops):
    # result = 0
    # for i in bus_stops:  # for i, o in bus_stops: ..... result += i - o....
    #     # result = result + int(i[0])-int(i[1])
    #     result = result + i[0] - i[1]  # result += i[0] - i[1]
    # return result
#    return sum([stop[0] - stop[1] for stop in bus_stops])
#    return [stop[0] - stop[1] for stop in bus_stops]
#    return sum(i - o for i, o in bus_stops)

    # get_in, get_off = zip(*bus_stops)
    # return sum(get_in) - sum(get_off)
    #
    # return sum(map(lambda x: x[0] - x[1], bus_stops))

    # num = zip(*bus_stops)
    # return sum(num[0]) - sum(num[1])

# bus_stops = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
# namber = lambda bus_stops: sum(i-o for i, o in bus_stops)
# print(namber(bus_stops))

# print(bus_stops)
# print(len(bus_stops))
# print('number', number(bus_stops))



"""A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more,
 is to arrange them into a square of square building blocks!

Квадрат из квадратов
Тебе нравятся строительные блоки. Вам особенно нравятся строительные блоки, которые представляют собой
квадраты. И что вам еще больше нравится, так это расположить их в квадрат из квадратных строительных блоков!

Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Учитывая целое число, определите, является ли это квадратным числом:
В математике квадратное число или совершенный квадрат - это целое число, которое является квадратом целого числа;
другими словами, это произведение некоторого целого числа на само себя.
В тестах всегда будет использоваться какое-то целое число, так что не беспокойтесь об этом в языках с динамической типизацией.
 """
# import math
# def is_square(n):
# #    return n > 0 and int(n ** 0.5) ** 2 == n
# #    return n > -1 and math.sqrt(n) % 1 == 0
#     return n >= 0 and (n**0.5) % 1 == 0
#
# n = 121
# print(is_square(n))
# x = 25
# z = math.sqrt(x).is_integer() # is_integer проверяет инт это или флоат или другое.
# print(z)

"""работа со строками примеры"""
# any_string = 'abrakadabra'
# a = 'a'
# ab = 'ab'
# ra = 'ra'
# # count считает сколько раз встречается символ или последовательность символов.
#
# print(any_string.count(a))
# print(any_string.count(ab))
# print(any_string.count(ra))
# # replace заменяет в строке символ или посл. символов на другую.
# new_any_string = any_string.replace(ab, '')
# new_any_string2 = any_string.replace('a', 'b', 2)
# print(new_any_string)
# print(new_any_string2)


"""All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the
same letters as the animal's name. For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed
to bring the dish to the feast.
Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces,
but these will not appear at the beginning or end of the string. They will not contain numerals.

Все животные устраивают пир! Каждое животное приносит одно блюдо. Есть только одно правило: блюдо должно начинаться и заканчиваться теми
 же буквами, что и название животного. Например, большая голубая цапля приносит чесночный наан, а синица - шоколадный торт.
Напишите функцию feast, которая принимает имя животного и блюдо в качестве аргументов и возвращает true или false, чтобы указать, разрешено ли животному
приносить блюдо на праздник.
Предположим, что beast и dish всегда являются строчными строками и что каждая из них содержит по крайней мере две буквы. зверь и блюдо могут содержать
дефисы и пробелы, но они не будут отображаться в начале или конце строки. Они не будут содержать цифр.
"""
# beast = 'great blue heron'
# dish = 'garlic naan'
# def feast(beast, dish):
#    return beast[0] == dish[0] and beast[-1] == dish[-1]
#   return beast.startswith(dish[0]) and beast.endswith(dish[-1])
#     return beast[::len(beast) - 1] == dish[::len(dish) - 1]

# if beast[0] == dish[0] and beast[-1] == dish[-1]:
#     print(True)
# else:
#     print(False)
# print(beast[::len(beast)-1])
# print(dish[0::len(dish)-1])
# print(feast(beast, dish))
# print(len(beast))
# print(beast[::])



""" You were camping with your friends far away from home, but when it's time to go back,
 you realize that your fuel is running out and the nearest pump is 50 miles away!
 You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.
Вы были в походе со своими друзьями далеко от дома, но когда приходит время возвращаться,
вы понимаете, что ваше топливо на исходе, а ближайшая заправка находится в 50 милях отсюда!
Вы знаете, что в среднем ваш автомобиль расходует около 25 миль на галлон. Осталось 2 галлона.
Учитывая эти факторы, напишите функцию, которая сообщает вам, возможно ли добраться до насоса или нет.
Функция должна возвращать значение true, если это возможно, и false, если нет.
"""


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left
#     return fuel_left * mpg >= distance_to_pump
#
# print(zero_fuel(50, 25,2))

# exec("".join(map(chr,[int("".join(str({':(': 4, ':/': 7, ':D': 1, '=/': 6, ':P': 2, '=)': 5, ';)': 9, ':)': 0, ':{': 8,
#                                        ':S': 3}[i]) for i in x.split())) for x in
# """:D :) :)  :D :) :D  :D :) :P  :S :P  :D :P :P  :D :) :D  :D :D :(  :D :D :D  :/ :)  :D :D
# :/  :D :) :D  :D :) :{  :( :)  :D :) :)  :D :) =)  :D :D =)  :D :D =/  ;) :/  :D :D :)  ;) ;)
# :D :) :D  ;) =)  :D :D =/  :D :D :D  ;) =)  :D :D :P  :D :D :/  :D :) ;)  :D :D :P  :( :(  :S
# :P  :D :) ;)  :D :D :P  :D :) :S  :( :(  :S :P  :D :) :P  :D :D :/  :D :) :D  :D :) :{  ;) =)
# :D :) :{  :D :) :D  :D :) :P  :D :D =/  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :P  :D :D
# :(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  :D :) :)  :D :) =)  :D :D =)  :D
# :D =/  ;) :/  :D :D :)  ;) ;)  :D :) :D  ;) =)  :D :D =/  :D :D :D  ;) =)  :D :D :P  :D :D :/
# :D :) ;)  :D :D :P  :S :P  =/ :)  =/ :D  :S :P  :D :) ;)  :D :D :P  :D :) :S  :S :P  :( :P  :S
# :P  :D :) :P  :D :D :/  :D :) :D  :D :) :{  ;) =)  :D :) :{  :D :) :D  :D :) :P  :D :D =/  :D :)"""
# .split("  ")])))

"""
Given an array of integer as strings and numbers, return the sum of the array values as
if all were numbers.
Return your answer as a number.
Учитывая массив целых чисел в виде строк и чисел, верните сумму значений массива,
как если бы все они были числами.
Верните свой ответ в виде числа.
"""

# def sum_mix(arr):
#     # sum1 = 0
#     # for i in arr:
#     #     # range(0, len(arr)):
#     #     i = int(i)
#     # return sum
#
#       return sum(map(int, arr))
#
#     # result = [int(i) for i in arr]
#     # result_sum = sum(result)
#     #print(result)
#     #    return sum
#     result = sum([int(i) for i in arr])

#     return result
#
# if __name__ == '__main__':
#     print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
