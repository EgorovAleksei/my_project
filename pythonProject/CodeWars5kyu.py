list1 = []
for i in range(5):
    list1.append([])
    for j in range(3):
        list1[i].append(0)


# list = [[0]*3]*5
# list1 = list[:]
# print(id(list), id(list1))

x = 0
for i in range(5):
    for j in range(3):
        x += 1
        list1[i][j] = x

# list1[4][0] = 0
# list1[4][1] = 0
# list1[4][2] = 0

print(list1)

""" нахождение 1 в соседних клетках
Учитывая массив строк, завершите функцию, вычислив общий периметр всех островов. Каждый участок суши будет отмечен буквой "X",
 в то время как водные поля будут представлены буквой "O". Считайте, что каждый раз это идеальный участок земли размером 1 х 1.
  Несколько примеров для лучшей визуализации:"""

#
# land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2
#
# def land_perimeter(a):
#     return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - land(a) - land(zip(*a)))
#
#
# def land_perimeter(arr):
#     I, J = len(arr), len(arr[0])
#
#     P = 0
#     for i in range(I):
#         for j in range(J):
#             if arr[i][j] == 'X':
#                 if i == 0 or arr[i - 1][j] == 'O': P += 1
#                 if i == I - 1 or arr[i + 1][j] == 'O': P += 1
#                 if j == 0 or arr[i][j - 1] == 'O': P += 1
#                 if j == J - 1 or arr[i][j + 1] == 'O': P += 1
#
#     return 'Total land perimeter: ' + str(P)

"""Вы были наняты крупным производителем MP3-плееров для внедрения нового стандарта сжатия музыки. В этой
 ката вы будете реализовывать КОДЕР, а сопутствующая ката имеет дело с ДЕКОДЕРОМ. Это можно считать более сложной
 версией извлечения диапазона.
Спецификация
Входной сигнал представляется в виде массива целых чисел. Несколько примеров закономерностей могут быть сокращены.
Последовательность из 2 или более одинаковых чисел сокращается как число*количество
Последовательность из 3 или более последовательных чисел сокращается как первое-последнее. Это верно как для восходящего, так и для нисходящего порядка
Последовательность из 3 или более чисел с одинаковым интервалом сокращается как first-last/interval. Обратите внимание, что интервал НЕ нуждается в знаке
Сжатие происходит слева направо
Примеры
[1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20] сжимается до "1,3-5,7-11,14,15,17-20 "
[0, 2, 4, 5, 7, 8, 9] сжимается до "0-4/2,5,7-9 "
[0, 2, 4, 5, 7, 6, 5] сжимается до "0-4/2,5,7-5 "
[0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5] сжимается до "0-4/2,5,7-5,5*4 "
Ввод
Непустой массив целых чисел

Выход
Строка целых чисел, разделенных запятыми, и дескрипторов последовательности"""

# raw = [6,4,2,1,1,1,1,3,4,5,7,6,5,4]
# res = ''
# res1 = ''
# res_rav = ''
# count = 0
# c = 0
# for i in range(len(raw)-1):
#     x = i
#     print('i=', i, 'c=', c)
#     if i > c:
#         while raw[x] - raw[x+1] == 2:
#             count += 1
#             c = c + 1
#             x = x + 1
#             if x == len(raw)-1:
#                 break
#         if count > 0:
#             res1 = res1 + f'{raw[i]}-{raw[x]},'
#             c = c + 1
#             count = 0
#
#         while raw[x] == raw[x+1]:
#             count += 1
#             c = c + 1
#             x = x + 1
#             if x == len(raw)-1:
#                 break
#
#         if count > 0:
#             res1 = res1 + f'{raw[i]}*{count + 1},'
#             count = 0
#
#         while raw[x] +1 == raw[x+1]:
#             count += 1
#             c = c + 1
#             x = x + 1
#             if x == len(raw)-1:
#                 break
#         if count > 0:
#             res1 = res1 + f'{raw[i]}-{raw[x]},'
#             c = c + 1
#             count = 0
#
#         while raw[x] - 1 == raw[x+1]:
#             count += 1
#             c = c + 1
#             x = x + 1
#             if x == len(raw)-1:
#                 break
#         if count > 0:
#             res1 = res1 + f'{raw[i]}-{raw[x]},'
#             c = c + 1
#             count = 0
#
# print(res1)
#
#
# def compress(raw):
#     # initialize stack
#     stack = [raw[0], raw[1]]
#     # calculate inital difference between the first two elements!
#     difference = stack[1] - stack[0]
#
#     out = []
#     for value in raw[2:] + [float("inf")]:
#         if (value - stack[-1]) == difference:
#             stack.append(value)
#
#         elif len(stack) > 1 and difference == 0:
#             out.append(f"{stack[0]}*{len(stack)}")
#             stack = [value]
#
#         elif len(stack) > 2:
#             absolute_difference = str(abs(difference))
#             out.append(f"{stack[0]}-{stack[-1]}{absolute_difference != '1' and '/' + absolute_difference or ''}")
#             difference = value - stack[-1]
#             stack = [value]
#         else:
#             if len(stack) == 2:  out.append(stack[0])
#             difference = value - stack[-1]
#             stack = [stack[-1], value]
#
#     # Handling possible leftovers in the stack
#     if not isinstance((f := stack[0]), float): out.append(f)
#     return ','.join(map(str, out))
#
#
# from collections import defaultdict
#
#
# def compress(raw):
#     same = lambda d, c, f, l: f"{f}*{c}"
#     one = lambda d, c, f, l: f"{f}-{l}"
#     stride = lambda d, c, f, l: f"{f}-{l}/{abs(d)}"
#     formatter = defaultdict(lambda: stride, [(0, same), (1, one), (-1, one)])
#
#     start, end = 0, 1
#     diff = raw[1] - raw[0]
#     output = []
#
#     while end < len(raw):
#         while end < len(raw) - 1 and raw[end + 1] - raw[end] == diff:
#             end += 1
#         count = end - start + 1
#         if diff == 0 or count >= 3:
#             output.append(formatter[diff](diff, count, raw[start], raw[end]))
#             start, end = end + 1, end + 2
#         else:
#             output.append(str(raw[start]))
#             start, end = end, end + 1
#         if end >= len(raw) or start >= len(raw): break
#         diff = raw[end] - raw[start]
#
#     if start < len(raw):
#         output.append(str(raw[start]))
#
#     return ",".join(output)
#
#
# def compress(raw):
#     raw = list(raw)
#     result = []
#     while raw:
#         # Identify sequence of indentical values or arithmetic sequence at start of raw
#         diff, l, i = None, 0, 0
#         for i, n in enumerate(raw[1:], 1):
#             if diff is None:
#                 # Initial difference
#                 diff = raw[i] - raw[i - 1]
#                 l = 1
#             elif diff != raw[i] - raw[i - 1]:
#                 # Difference sequence has ended
#                 break
#             else:
#                 # Difference sequence continues
#                 l += 1
#
#         # Encode the values into the output string
#         if i == 0:
#             # Only one digit left
#             result.append(str(raw.pop(0)))
#         elif diff == 0:
#             # Sequence of identical numbers
#             result.append(f'{raw[0]}*{l + 1}')
#             raw = raw[l + 1:]
#         elif l == 1:
#             # No sequence, so single number
#             result.append(str(raw.pop(0)))
#         elif l > 1:
#             if diff in [-1, 1]:
#                 # Sequence of +1 or -1
#                 result.append(f'{raw[0]}-{raw[l]}')
#             else:
#                 # Sequence of >+1 or <-1
#                 result.append(f'{raw[0]}-{raw[l]}/{abs(diff)}')
#             raw = raw[l + 1:]
#
#     print(','.join(result))
#     return ','.join(result)



"""Программное обеспечение для распознавания символов широко используется для оцифровки печатных текстов. Таким образом,
тексты можно редактировать, искать и сохранять на компьютере.
Когда документы (особенно довольно старые, написанные на пишущей машинке) оцифровываются, программы распознавания символов
 часто допускают ошибки. Ваша задача - исправить ошибки в оцифрованном тексте. Вам нужно только справиться со следующими ошибками:
 S is misinterpreted as 5   O is misinterpreted as 0   I is misinterpreted as 1
Тестовые примеры содержат цифры только по ошибке."""

# s ="L0ND0N"
#
# def correct(s):
#     sl = {'0':'O', '1':'I', '5':'S'}
#     return ''.join(sl[i]  if i == '0' or i == '1' or i == '5' else i for i in s)
#     return s.translate(str.maketrans("501", "SOI"))
#     return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')
#
# print(correct(s))

"""В этом ката вы создадите функцию, которая принимает список неотрицательных целых чисел и строк и возвращает новый
 список с отфильтрованными строками.
 filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
 """
# l = [1, 2, 'a', 'b']
# def filter_list(l):
#     return [i  for i in l if type(i) == int]
# return [e for e in l if isinstance(e, int)]
# print(filter_list(l))


"""Давным-давно, на пути через старый дикий горный запад,…
...человеку дали указания, как пройти из одной точки в другую. Направления были "СЕВЕР", "ЮГ", "ЗАПАД", "ВОСТОК".
Очевидно, что "СЕВЕР" и "ЮГ" противоположны, "ЗАПАД" и "ВОСТОК" тоже.
Идти в одном направлении и сразу же возвращаться в противоположном направлении - это ненужное усилие. Поскольку это
 дикий запад, с ужасной погодой и небольшим количеством воды, важно экономить немного энергии, иначе вы можете умереть от жажды!
Как я с умом пересек гористую пустыню.
Указания, данные мужчине, являются, например, следующими (в зависимости от языка):
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
Вы сразу видите, что идти "на СЕВЕР" и сразу "на ЮГ" неразумно, лучше оставайтесь на том же месте! Итак, задача состоит в
том, чтобы дать мужчине упрощенный вариант плана. Лучший план в этом случае - это просто:
["WEST"]   or   { "WEST" }  or  [West]
В ["СЕВЕР", "ЮГ", "ВОСТОК", "ЗАПАД"] направление "СЕВЕР" + "ЮГ" идет на север и сразу возвращается.
Путь становится ["ВОСТОК", "ЗАПАД"], теперь "ВОСТОК" и "ЗАПАД" уничтожают друг друга, следовательно, конечный
результат равен [] (ноль в Clojure).
В ["СЕВЕР", "ВОСТОК", "ЗАПАД", "ЮГ", "ЗАПАД", "ЗАПАД"] "СЕВЕР" и "ЮГ" не являются прямо противоположными,
но они становятся прямо противоположными после сокращения "ВОСТОК" и "ЗАПАД", так что весь путь сводим на ["ЗАПАД", "ЗАПАД"].
Задача
Напишите функцию dirReduc, которая примет массив строк и вернет массив строк с удаленными ненужными указаниями
(W<->E или S<->N рядом).
Версия Haskell принимает список направлений с направлением данных = Север | Восток | Запад | Юг.
Версия Clojure возвращает nil, когда путь сводится к нулю.
Версия Rust использует фрагмент направления перечисления {Север, Восток, Запад, Юг}.
Смотрите больше примеров в разделе "Примеры тестов:"
Записи
Не все пути можно упростить. Путь ["СЕВЕР", "ЗАПАД", "ЮГ", "ВОСТОК"] не сводим. "СЕВЕР" и "ЗАПАД", "ЗАПАД" и "ЮГ",
"ЮГ" и "ВОСТОК" не являются прямой противоположностью друг другу и не могут стать таковыми. Следовательно,
результирующий путь сам по себе: ["СЕВЕР", "ЗАПАД", "ЮГ", "ВОСТОК"].
если вы хотите перевести, пожалуйста, спросите перед переводом.  """
# arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# x = 10
# sl = {
#     'NORTH': 'SOUTH',
#     'SOUTH': 'NORTH',
#     'EAST': 'WEST',
#     'WEST': 'EAST',
# }
#
# print(sl['NORTH'])

# def dirReduc(arr):
#     if len(arr) >1:
#         for i in range(len(arr)-1):
#             print(i)
#             if arr[i] == sl[arr[i+1]]:
#                 arr.pop(i+1)
#                 arr.pop(i)
#                 return dirReduc(arr)
#     return arr
#
#
# def dirReduc(arr):
#     opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
#
#     for i in range(len(arr) - 1):
#         if set(arr[i:i + 2]) in opposites:
#             del arr[i:i + 2]
#             return dirReduc(arr)
#
#     return arr
#
#
# print( dirReduc(arr))


"""Кто помнит свое время на школьном дворе, когда девочки брали цветок и рвали его лепестки, произнося каждую
из следующих фраз каждый раз, когда отрывался лепесток:
"Я люблю тебя"    "немного"    "очень много"    "страстно"    "безумно"   "вовсе нет"
Если лепестков больше 6, вы начинаете сначала с "Я люблю тебя" для 7 лепестков, "немного" для 8 лепестков и так далее.
Когда был сорван последний лепесток, раздались крики возбуждения, мечты, нахлынувшие мысли и эмоции.
Ваша цель в этом ката - определить, какую фразу девушки произнесли бы на последнем лепестке для цветка с заданным
 количеством лепестков. Количество лепестков всегда больше 0."""

# petals = \
#     {
#         1: "I love you",
#         2: "a little",
#         3: "a lot",
#         4: "passionately",
#         5: "madly",
#         0: "not at all"
#
# }
#
# nb_petals = 6
# print(petals[2])
# def how_much_i_love_you(nb_petals):
#     return petals[nb_petals % 6]
#     return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]
# print(how_much_i_love_you(333))

"""Добро пожаловать. В этом ката вас просят возвести в квадрат каждую цифру числа и объединить их.
Например, если мы запустим 9119 через функцию, получится 811181, потому что 92 равно 81, а 12 равно 1.
Примечание: Функция принимает целое число и возвращает целое число"""

# num = 9119
# def square_digits(num):
#     return int(''.join(str(int(i)**2) for i in str(num)))
# print(square_digits(num))

"""Напишите функцию, которая принимает массив чисел (целых чисел для тестов) и целевой номер. Он должен найти
два разных элемента в массиве, которые при сложении вместе дают целевое значение. Индексы этих элементов затем
должны быть возвращены в виде кортежа / списка (в зависимости от вашего языка) следующим образом: (index1, index2).
Для целей этого ката некоторые тесты могут иметь несколько ответов; будут приняты любые допустимые решения.
Входные данные всегда будут действительными (числа будут представлять собой массив длиной 2 или больше, и все элементы
 будут числами; цель всегда будет суммой двух разных элементов из этого массива)."""

# numbers = [1,2,3]
# target = 4
# def two_sum(numbers, target):
#     for ind, val in enumerate(numbers):
#         if target - val in numbers:
#             for ind2 in range(ind+1, len(numbers)):
#                 if numbers[ind2] == target - val:
#                     return [ind, ind2]
# def two_sum(nums, t):
#     for i, x in enumerate(nums):
#         for j, y in enumerate(nums):
#             if i != j and x + y == t:
#                 return [i, j]
# print(two_sum(numbers, target))
"""На этот раз мы хотим записать вычисления с использованием функций и получить результаты.
Давайте взглянем на некоторые примеры:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Требования:
Для каждого числа от 0 ("ноль") до 9 ("девять") должна быть функция
Должна быть функция для каждой из следующих математических операций: плюс, минус, раз, деление_by
Каждое вычисление состоит ровно из одной операции и двух чисел
Самая внешняя функция представляет левый операнд, самая внутренняя функция представляет правый операнд
Деление должно быть целочисленным делением. Например, это должно возвращать 2, а не 2.666666...:
"""
# def _digit(namber, operator = None):
#     if operator is None:
#         return namber
#     return operator(namber)
# def zero(operator = None): return _digit(0, operator)
# def one(operator = None): return _digit(1, operator)
# def two(operator = None): return _digit(2, operator)
# def three(operator = None): return _digit(3, operator)
# def four(operator = None): return _digit(4, operator)
# def five(operator = None): return _digit(5, operator)
# def six(operator = None): return _digit(6, operator)
# def seven(operator = None): return _digit(7, operator)
# def eight(operator = None): return _digit(8, operator)
# def nine(operator = None): return _digit(9, operator)
#
# def plus(second_operand): return lambda first_operand: first_operand + second_operand
# def minus(second_operand): return lambda first_operand: first_operand - second_operand
# def times(second_operand): return lambda first_operand: first_operand * second_operand
# def divided_by(second_operand): return lambda first_operand: int(first_operand / second_operand)

# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y


# print(seven(plus(seven())))
# print(seven(times(five())))
"""Напишите функцию для разделения строки и преобразования ее в массив слов."""
# s = ""
# print(s.split(' '))
"""Реализуйте алгоритм псевдошифрования, который, учитывая строку S и целое число N, объединяет все символы с
нечетным индексом S со всеми символами с четным индексом S, этот процесс следует повторить N раз.
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Вместе с функцией шифрования вы также должны реализовать функцию дешифрования, которая обращает процесс вспять.
Если строка представляет собой пустое значение или целое число N не является положительным, верните первый аргумент
 без изменений.
"""
# text = "This is a test!"
# de_text = "hsi  etTi sats!"
# n = 1
# text_new = ''
# # for i in range(n):
# #     text = text[1::2] + text[::2]
#
# for i in range(n):
#     text_new = ''
#     x = len(encrypted_text) // 2
#     for c in range(x):
#         text_new = text_new + encrypted_text[x + c] + encrypted_text[c]
#     text_new = text_new + encrypted_text[:x * 2 - 1:-1]
#     encrypted_text = text_new
# return text_new if n > 0 else encrypted_text
#
#
# print(de_text)


"""Хорошо познакомился со старшим братом Фибоначчи, он же Трибунат.
Как уже может показаться из названия, он работает в основном как Фибоначчи, но суммирует последние 3
 (вместо 2) числа последовательности, чтобы сгенерировать следующее. И, что еще хуже, к сожалению, я не услышу,
 как люди, не являющиеся носителями итальянского языка, пытаются произнести это:(
Итак, если мы хотим начать нашу последовательность Tribonacci с [1, 1, 1] в качестве начального ввода (он же сигнатура),
 у нас есть эта последовательность:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
Но что, если мы начнем с [0, 0, 1] в качестве подписи? Поскольку начало с [0, 1] вместо [1, 1] в основном сдвигает
общую последовательность Фибоначчи на одно место, у вас может возникнуть соблазн подумать, что мы получим ту же
 последовательность, сдвинутую на 2 места, но это не так, и мы получим:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Что ж, возможно, вы уже догадались об этом, но для ясности: вам нужно создать функцию Фибоначчи, которая,
 учитывая массив сигнатур / список, возвращает первые n элементов - сигнатур, включенных в последовательность so seeded.
Подпись всегда будет содержать 3 числа; n всегда будет неотрицательным числом; если n == 0, то верните пустой массив
(за исключением C return NULL) и будьте готовы ко всему остальному, что четко не указано ;) """
# signature = [1, 1, 1]
# n = 10
# for i in range(2, n-1):
#     signature.append(signature[i-2] + signature[i-1] + signature[i])
#
# def tribonacci(signature, n):
#     for i in range(2, n-1):
#         signature.append(signature[i-2] + signature[i-1] + signature[i])
#     return signature[:n:]
#
# print(tribonacci(signature, n))



"""Создайте функцию с двумя аргументами, которая вернет массив из первых n кратных x.
Предположим, что и заданное число, и количество раз для подсчета будут положительными числами, большими 0.
Возвращает результаты в виде массива или списка (в зависимости от языка ).
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
"""
# x = 3
# n = 5
# def count_by(x, n):
#     res = []
#     i = 0
#     while len(res) < n:
#         i += 1
#         if i % x == 0:
#             res.append(i)
#     return res
# return range(x, x * n + 1, x)
# return [i * x for i in range(1, n + 1)]
# print(count_by(x,n))

"""Цель этого упражнения - преобразовать строку в новую строку, где каждый символ в новой строке равен "(",
 если этот символ появляется только один раз в исходной строке, или ")", если этот символ появляется более одного
 раза в исходной строке. Игнорируйте заглавные буквы при определении того, является ли символ дубликатом.
 Examples
"din"      =>  "((("   "recede"   =>  "()()()"  "Success"  =>  ")())())"  "(( @"     =>  "))(("
В сообщениях с утверждениями может быть неясно, что они отображают на некоторых языках. Если вы читаете"...Он должен
кодировать XXX", "XXX" - это ожидаемый результат, а не входные данные! """

# word = "rEcede"
# def duplicate_encode(word):
#     return ''.join('(' if word.lower().count(i) <= 1 else ')' for i in word.lower())
# print(duplicate_encode(word))

"""Напишите функцию, которая проверяет, является ли заданная строка (без учета регистра) палиндромом"""

# s = 'aaabbaaa'
#
# if s[0:len(s) // 2].lower() == s[::-1][0:(len(s) // 2)].lower():
#     print(s)
# def is_palindrome(s):
#     return s.lower() == s[::-1].lower()
#
# print(is_palindrome(s))
"""Чтобы быть старшим, устнику должно быть не менее 55 лет и иметь гандикап больше 7. В этом крокетном клубе
 гандикапы варьируются от -2 до +26; чем лучше игрок, тем ниже гандикап.
Ввод Входные данные будут состоять из списка пар. Каждая пара содержит информацию для одного потенциального участника.
Информация состоит из целого числа для возраста человека и целого числа для инвалидности человека.
Выход Выходные данные будут состоять из списка строковых значений (в Haskell и C: Open или Senior), указывающих,
должен ли соответствующий элемент быть помещен в категорию senior или open.
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]"""

# data = [(45, 12),(55,21),(19, -2),(104, 20)]
#
# def open_or_senior(data):
#     return ['Senior' if (i >= 55 and x > 7) else 'Open' for i,x in data]

"""Ваша команда пишет новый модный текстовый редактор, и вам было поручено внедрить нумерацию строк.
Напишите функцию, которая принимает список строк и возвращает каждую строку, перед которой стоит правильный номер.
Нумерация начинается с 1. Формат - n: string. Обратите внимание на двоеточие и пробел между ними.
Examples: (Input --> Output)
[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]"""

# lines = []
# def number(lines):
#     return [str(i+1)+ ': ' + lines[i] for i in range(len(lines))]
# print(number(lines))
""" Банкоматы допускают 4- или 6-значные PIN-коды, а PIN-коды не могут содержать ничего, кроме ровно 4 цифр или ровно 6 цифр.
Если функции передана допустимая строка PIN-кода, верните значение true, в противном случае верните значение false. """
# pin = '-234'
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
# print(validate_pin(pin))
""" Вам дается массив целых чисел нечетной длины, в котором все они одинаковы, за исключением одного-единственного числа.
Завершите метод, который принимает такой массив, и вернет это единственное другое число.
Входной массив всегда будет действительным! (нечетная длина >= 3) """
# arr = [1, 1, 1, 1, 1, 1, 2]
#
# for i in set(arr):
#     if arr.count(i) == 1:
#         print(i)
# return i for i in set(arr) if arr.count(i) == 1  # НЕ РАБОТАЕТ передевать надо что-то целое
# return [i for i in set(arr) if arr.count(i) == 1][0] #РАБОТАЕТ Передает число из списка с индексом 0
# return min(arr, key=arr.count)

"""Вам дается массив (список) strarr строк и целое число k. Ваша задача состоит в том, чтобы вернуть первую
самую длинную строку, состоящую из k последовательных строк, взятых в массиве.
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n - длина массива строк, если n = 0 или k > n или k <= 0 возвращает "" (ничего не возвращает в Elm, "ничего" в Erlang).
Обратите внимание на последовательные строки: следуйте одна за другой без перерыва"""
#
# strarr = ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
# k = 2
#
# def longest_consec(strarr, k):
#     res = ''
#     if len(strarr) > k and k >= 0 and len(strarr) >= 0:
#         res1 = ''
#         for i in range(len(strarr) - k +1):
#             res1 = ''
#             for c in range(k):
#                 res1 = res1 + strarr[c + i]
#                 if len(res1) > len(res):
#                     res = res1
#     return res
#
#     result = ""
#
#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index + k])
#             if len(s) > len(result):
#                 result = s
#
#     return result
#
#     if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
#         return ""
#     lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
#     return max(lst, key= lambda x: len(x))
#
#     n = len(s)
#     if n == 0 or k > n or k <= 0:
#     	return ''
#     return sorted([''.join(s[i:i+k]) for i in range(0, n-k+1)], key=len, reverse=True)[0]
#
# print(longest_consec(strarr, k))
""" ROT13 - это простой шифр подстановки букв, который заменяет букву буквой 13 букв после нее в алфавите. ROT13 -
это пример шифра Цезаря.
Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если в строку
включены цифры или специальные символы, они должны быть возвращены в том виде, в каком они есть.
Только буквы из латинского / английского алфавита должны быть сдвинуты, как в оригинальной "реализации" Rot13.
Пожалуйста, обратите внимание, что использование encode считается мошенничеством. """

# message = 'test!!!'
# rot = {'a':'n', 'A':'N', 'b':'o', 'B':'O', 'c':'p', 'C':'P', 'd':'q', 'D':'Q', 'e':'r', 'E':'R', 'f':'s', 'F':'S', 'g':'t', 'G':'T',
#     'h':'u', 'H':'U', 'i':'v', 'I':'V', 'j':'w', 'J':'W', 'k':'x', 'K':'X', 'l':'y', 'L':'Y', 'm':'z', 'M':'Z', 'n': 'a', 'N':'A',
#     'o':'b', 'O':'B', 'p':'c', 'P':'C', 'q':'d', 'Q':'D', 'r':'e', 'R':'E', 's':'f', 'S':'F', 't':'g', 'T':'G', 'u':'h', 'U':'H',
#     'v':'i', 'V':'I', 'w':'j', 'W':'J', 'x':'k', 'X':'K', 'y':'l', 'Y':'L', 'z':'m', 'Z':'M'
#          }
# #rot = {'a': 'n', 'A': 'N', 'b': 'o'}
#
# def rot13(message):
#     res = ''
#     for i in message:
#         try:
#             if rot[i]:
#                 res = res + rot[i]
#         except KeyError:
#             res = res + i
#     print(res)
#
# return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
# print(rot13(message))



""" 
история: Боб работает водителем автобуса. Однако он стал чрезвычайно популярен среди жителей города.
С таким количеством пассажиров, желающих попасть на борт его автобуса, ему иногда приходится сталкиваться с
проблемой нехватки места в автобусе! Он хочет, чтобы вы написали простую программу, сообщающую ему, сможет ли он
вместить всех пассажиров.
Обзор задач:
Вы должны написать функцию, которая принимает три параметра:
ограничение - это количество людей, которое может вместить автобус, исключая водителя.
вкл. - это количество людей в автобусе, исключая водителя.
ожидание - это количество людей, ожидающих посадки в автобус, исключая водителя.
Если места достаточно, верните 0, а если нет, верните количество пассажиров, которых он не может взять.
 Usage Examples:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting """
# def enough(cap, on, wait):
#     return 0 if cap - on >= wait else wait - cap + on
#     return max(0, wait - (cap - on))

""" Функция записи Удаляет восклицательные знаки, которая удаляет все восклицательные знаки из заданной строки. """
# s = "!H!e!l!l!o!!!! W!o!rld!"
# def remove_exclamation_marks(s):
#     return ''.join(x for x in s if x != '!')
#     return s.replace('!', '')
# print(remove_exclamation_marks(s))

""" Число 89 - это первое целое число с более чем одной цифрой, которое удовлетворяет свойству, частично
представленному в названии этого ката. Какой смысл говорить "Эврика"? Потому что эта сумма дает одно и то же число.
В действительности: 89 = 8^1 + 9^2
Следующее число, обладающее этим свойством, - 135.
Посмотрите на это свойство еще раз: 135 = 1^1 + 3^2 + 5^3
Нам нужна функция для сбора этих чисел, которая может принимать два целых числа a, b, определяющая диапазон [a, b]
(включительно) и выводящая список отсортированных чисел в диапазоне, который удовлетворяет свойству, описанному выше.
Давайте посмотрим на некоторые случаи (ввод -> вывод):
 1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.
90, 100 --> []"""
# a = 11
# b = 50
# s = 'strit'
# res_list = []
# def sum_dig_pow(a, b):
#     for i in range(a, b+1):
#         res_p = 0
#         res = [int(x) for x in str(i)]
#         for c in range (len(str(i))):
#             res_p = res_p + res[c]**(c+1)
#             if res_p == i:
#                 res_list.append(i)
#     return res_list
# return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]
#
# print(sum_dig_pow(a, b))

""" Напишите функцию persistence, которая принимает положительный параметр num и возвращает его мультипликативную
настойчивость, то есть количество раз, которое вы должны умножить цифры в num, пока не достигнете единственной цифры.
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)  """

# import math
# n = 999
# def persistence(n):
#     count = 0
#     while n > 9:
#         res = [int(x) for x in str(n)]
#         n = math.prod(res)
#         count += 1
#     print(count)
#
# from operator import mul
# def persistence(n):
#     return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1
#
# print(persistence(n))


""" Ваша цель в этом ката - реализовать функцию разности, которая вычитает один список из другого и
возвращает результат. Он должен удалить все значения из списка a, которые присутствуют в списке b,
сохраняя их порядок.
массив_diff([1,2],[1]) == [2]
Если значение присутствует в b, все его вхождения должны быть удалены из другого:
массив_diff([1,2,2,2,3],[2]) == [1,3] """
# a = [1,2,2, 4, 5, 2, 4, 9]
# b =[4, 5]
# def array_diff(a, b):
#     return [i for i in a if i not in b]
# print(array_diff(a, b))


""" Задача подмассива с максимальной суммой состоит в нахождении максимальной суммы непрерывной
подпоследовательности в массиве или списке целых чисел: максимальная последовательность([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# должно быть 6: [4, -1, 2, 1]
Простой случай - это когда список состоит только из положительных чисел, а максимальная сумма равна сумме всего массива.
Если список состоит только из отрицательных чисел, верните вместо этого 0. Считается, что пустой список имеет нулевую
наибольшую сумму. Обратите внимание, что пустой список или массив также является допустимым подсписком/подмассивом. """

# arr = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
#arr =[2, 2, -2, 1, -3, 4, -1, -10, 10, 10,  -5, -6, -4, 14]
# max = 0
# for i in range(len(arr)):
#     res = 0
#     res = arr[i]
#     if arr[i] > 0:
#         for c in range(i+1, len(arr)):
#             res = sum(arr[i:c+1])
#             if res > max:
#                 max = res
# слишком долгое решение

    # maximum = 0
    # local_maximum = 0
    # for i in arr:
    #     if local_maximum > 0:
    #         local_maximum += i
    #         if local_maximum < 0:
    #             local_maximum = 0
    #         elif local_maximum > maximum:
    #             maximum = local_maximum
    #     elif i > 0:
    #         local_maximum += i
    #
    # return maximum
    # скачал с инета, не все тесты проходит

# def maxSequence(arr):
#     max = 0
#     curr = 0
#     for x in arr:
#         curr+=x
#         if curr<0:
#             curr=0
#         if curr>max:
#             max=curr
#     return max
#
# print(maxSequence(arr))

""" Основная идея состоит в том, чтобы подсчитать все встречающиеся символы в строке. Если у вас есть строка,
подобная aba, то результатом должно быть {'a': 2, 'b': 1}.
Что делать, если строка пуста? Тогда результатом должен быть пустой объектный литерал, {}. """

# s = 'abasdfsdfasdf'
# res = {}

# def count(s):
#     # res = {}
#     # return [{} if not s else res[i] = s.count(i) for i in set(s)]  # не работает ((((
#     # return {i: string.count(i) for i in string}  # Работает
#     # return {x: s.count(x) for x in set(s)}
#     return {i: s.count(i) for i in s}
# print(count(s))
#
# for i in s:
#     res[i] = s.count(i)
# print(res)



""" Завершите функцию квадратной суммы так, чтобы она возводила в квадрат каждое переданное в нее число,
а затем суммировала результаты вместе.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9."""

# x = [0, 3, 4, 5]
# print(sum(list(map(lambda x: x**2, x))))
# print(sum(map(lambda x: x**2, x)))
# return sum(x ** 2 for x in numbers)

""" Если ты не можешь уснуть, просто посчитай овец!! Задача:
Учитывая неотрицательное целое число, например 3, верните строку с бормотанием: "1 овца ... 2 овцы ... 3 овцы ...".
Входные данные всегда будут действительными, т.е. никаких отрицательных целых чисел. """
# n = 3
# def count_sheep(n):
#     return ''.join(f'{i} sheep...' for i in range(1, n+1))
#
# print(count_sheep(n))


""" Вам даны длина и ширина 4-стороннего многоугольника. Многоугольник может быть либо прямоугольником, либо квадратом.
Если это квадрат, верните его площадь. Если это прямоугольник, верните его периметр. Example(Input1, Input2 --> Output):
6, 10 --> 32  3, 3 --> 9 """
# def area_or_perimeter(l , w):
#     return l*w if l == w else 2*l + 2*w
#     return [(l+w)*2, l*w][(l == w)]