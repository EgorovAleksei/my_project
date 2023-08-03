

""" Волна (известная как мексиканская волна в англоязычном мире за пределами Северной Америки) является примером метахронного ритма, достигаемого на переполненном стадионе, когда последовательные группы зрителей ненадолго встают, кричат и поднимают руки. Сразу же после вытягивания в полный рост зритель возвращается в обычное сидячее положение.
В результате образуется волна стоящих зрителей, которая проходит через толпу, хотя отдельные зрители никогда не покидают своих мест. На многих больших аренах толпа рассаживается непрерывным кольцом по всему спортивному полю, и поэтому волна может непрерывно перемещаться по арене; при несмежном расположении сидячих мест волна может вместо этого отражаться назад и вперед через толпу. Когда зазор в посадочных местах узкий, волна иногда может проходить через него. Обычно в любой момент времени на арене присутствует только один гребень волны, хотя были созданы одновременные волны, вращающиеся в противоположных направлениях.
Задача В этом простом Ката ваша задача - создать функцию, которая превращает строку в мексиканскую волну.
Вам будет передана строка, и вы должны вернуть эту строку в массиве, где заглавная буква - это человек, стоящий.
Правила  1. Входная строка всегда будет строчной, но, возможно, пустой.
 2. Если символ в строке является пробелом, то передайте его так, как если бы это было пустое место
Пример  wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"] """


# def wave(x):
#     # return [ x[0:i:].lower() + x[i].upper() + x[i+1:len(x):] for i in range(len(x)) if x[i] != ' ' ] #правильно
#     return [ x[:i].lower() + x[i].upper() + x[i+1:] for i in range(len(x)) if x[i] != ' ' ] # правильно, удалил лишнее
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
#     return [f'{s[:i]}{s[i].upper()}{s[i+1:]}' for i,x in enumerate(s) if x != ' ']
# print(wave(x))




"""Учитывая непустой массив целых чисел, верните результат умножения значений вместе по порядку. 
Пример: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""

# import math
# arr = [2, 2, 2, 2, 2, 2]
# def grow(arr):
#     return math.prod(arr)

from math import prod as grow
#
# print(math.prod(arr))

""" Теги: макс и мин, или максимум и так далее. зависит от языка ) это получает список целых чисел в качестве
входных данных и возвращает наибольшее и наименьшее число в этом списке соответственно.
Другие примеры (Входные данные)  * [4,6,2,1,9,63,-134,566] -> макс = 566, мин = -134
* [-52, 56, 30, 29, -54, 0, -110] -> разъем = 110, макс = 56  * [42, 54, 65, 87, 0] -> x = 0, макс = 87
[5] - мин = 5, макс = 5  """

# arr = [-52, 56, 30, 29, -54, 0, -110]
# print(max(arr))
#
# def minimum(arr):
#     return min(arr)
#
# def maximum(arr):
#     return max(arr)
#
# minimum = min
# maximum = max

""" Возьмите массив и удалите каждый второй элемент из массива. Всегда сохраняйте первый элемент и начинайте удаление
со следующего элемента. Пример: ["Сохранить", "Удалить", "Сохранить", "Удалить", "Сохранить", ...] --> ["Сохранить", "Сохранить", "Сохранить", ...]
Ни один из массивов не будет пустым, так что вам не нужно беспокоиться об этом!"""

# my_list = ['Hello', 'Goodbye', 'Hello Again']
# my_list1 = 'sdlfkdsfaAAA'
# print(my_list1[::-1])

# for i in range(len(my_list)):
#     if i % 2 == 0:
#         my_list1.append(my_list[i])
#         print(i)
# print(my_list1)

# def remove_every_other(my_list):
#     return [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
#     return [v for c, v in enumerate(my_list) if not c % 2]
#     return [my_list[i] for i in range(0, len(my_list), 2)]
#     return my_list[::2]
#
# print(remove_every_other(my_list))

""" Вы получаете массив чисел, возвращаете сумму всех положительных чисел. Пример [1,-4,7,12] => 1 + 7 + 12 = 20
Примечание: если суммировать нечего, сумма по умолчанию равна 0. """
#
# arr = [-1,-2,-3,-4,-5]
# def positive_sum(arr):
#     return sum(i for i in arr if i > 0)
# print(positive_sum(arr))

"""Завершите решение так, чтобы функция разбила верблюжью оболочку, используя пробел между словами.
Пример "camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""  """""
# s = "helloWorld"
# s1 = ''
# for i in s:
#     if ord(i) < 90:
#         s1 = s1 + ' ' + i
#     else:
#         s1 = s1 + i
# print(s1)
# # ''.join('0' if c < '5' else '1' for c in x)
# def solution(s):
#     return ''.join(i if ord(i)>90 else ' ' + i  for i in s )
# return re.sub('([A-Z])', r' \1', s)
# return re.sub(r"([a-z])([A-Z])", r"\1 \2", stg)
#
#
# print(solution(s))

""" Натан любит кататься на велосипеде. Поскольку Натан знает, как важно поддерживать гидратацию, он выпивает 0,5 литра воды за час езды на велосипеде.
Вам дается время в часах, и вам нужно вернуть количество литров, которые выпьет Натан, округленное до наименьшего значения.
Например:  время = 3 ---- > литров = 1  время = 6,7---> литров = 3  время = 11,8--> литров = 5 """
#
# def litres(time):
#     return time // 2


""" Учитывая последовательность слов, вам нужно найти слово, набравшее наибольшее количество баллов.
Каждая буква слова набирает очки в соответствии с ее положением в алфавите: a = 1, b = 2, c = 3 и т.д.
Вам нужно вернуть слово с наивысшим баллом в виде строки.
Если два слова набирают одинаковый балл, верните слово, которое появляется раньше всего в исходной строке.
Все буквы будут строчными, и все входные данные будут действительными. """

# x = 'what time are we climbing up the volcano'
# y = x.split()
# z = []
# print(y)
#
# for i in y:
#     count = 0
#     for c in i:
#         count = count + ord(c) - 96
#     z.append(count)
# print(z)
# print(y[z.index(max(z))])
#
# return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

"""Таракан - одно из самых быстрых насекомых. Напишите функцию, которая принимает его скорость в километрах в час
и возвращает ее в сантиметрах в секунду, округленную до целого числа (= floored). Например:
1.08 --> 30 Обратите внимание! Входные данные представляют собой действительное число (фактический тип зависит от языка) и равны >= 0. Результатом должно быть целое число."""
#
# x = 1.09
# y = x*1000*100/60/60
# print(int(y))
#
# def cockroach_speed(s):
#     return int(s*1000/6/6)

"""Реализуйте функцию, которая складывает два числа вместе и возвращает их сумму в двоичном формате. Преобразование может
быть выполнено до или после добавления. Возвращаемое двоичное число должно быть строкой.
Примеры: (Ввод1, Ввод2 --> Вывод (объяснение)))
1, 1 --> "10" (1 + 1 = 2 в десятичной системе счисления или 10 в двоичной)
5, 9 --> "1110" (5 + 9 = 14 в десятичной системе счисления или 1110 в двоичной системе счисления)"""

# x = 14
# print(f'{x:b}')
#
# def add_binary(a,b):
#     # return bin(a + b)[2:]
#     return f'{a + b:b}'
#
# print(add_binary(51,12))

"""Рассмотрим массив / список овец, где некоторые овцы могут отсутствовать на своем месте. Нам нужна функция, которая
подсчитывает количество овец, присутствующих в массиве (true означает присутствует)."""

# sheep = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,        True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,                  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,         False, False, False, False, False, False, False, False, False, False]

#
# def count_sheeps(sheep):
#     # return sum(x for x in sheep if x)
#     return sheep.count(True)
# print(count_sheeps(sheep))


"""Учитывая массив (arr) в качестве аргумента, завершите функцию подсчета смайликов, которая должна возвращать общее количество улыбающихся лиц.
Правила для улыбающегося лица:
Каждый смайлик должен содержать действительную пару глаз. Глаза могут быть помечены как : или ;
У смайлика может быть нос, но это не обязательно. Допустимыми символами для носа являются - или ~
На каждом улыбающемся лице должен быть улыбающийся рот, который должен быть отмечен либо ), либо D
Никакие дополнительные символы, кроме упомянутых, не допускаются.
Допустимые примеры смайликов : :) :D ;-D :~)
Недопустимые смайлики: ;( :> :} :]"""

# arr = [':)',':(',':D',':O',':;']
# smile = [':D', ';D', ':)', ';)', ':~)', ':~D', ';~D', ';~)', ';-D', ':-D',  ';-)', ':-)']
# def count_smileys(arr):
#    return len([c for c in arr if c in smile])
#    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
#    return sum(1 for s in arr if re.match(r'\A[:;][-~]?[)D]\Z', s))
# print(count_smileys(arr))

"""Камень Ножницы Бумага Давайте играть! Вы должны вернуть, какой игрок выиграл! В случае ничьей повторите ничью!.
"scissors", "paper" --> "Player 1 won!"    "scissors", "rock" --> "Player 2 won!" "paper", "paper" --> "Draw!" """
# p1 = 'scissors'
# p2 = 'rock'
#
# def rps(p1, p2):
#     if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
#         return "Player 1 won!"
#     elif (p1 == 'scissors' and p2 == 'rock') or (p1 == 'rock' and p2 == 'paper') or (p1 == 'paper' and p2 == 'scissors') :
#         return 'Player 2 won!'
#     else:
#         return 'Draw!'
#
# print(rps(p1, p2))

"""Ваша задача - преобразовать строки так, как они были бы написаны Джейденом Смитом. Строки представляют собой настоящие цитаты из
 Джейдена Смита, но они написаны не с заглавной буквы так, как он первоначально их набрал.
Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real" """

# string = "How can mirrors be real if our eyes aren't real"
#
# # def to_jaden_case(string):
# #     return ' '.join(i.capitalize() for i in string.split())
# import string
# toJadenCase = string.capwords
# return ' '.join(map(str.capitalize, string.split()))


"""Описание: Создайте простую функцию под названием greet, которая возвращает самое известное "привет, мир!".
Точки стиля  Конечно, это настолько просто, насколько это возможно. Но насколько умным вы можете быть, чтобы создать самый креативный hello world,
о котором только можете подумать? Какое решение "hello world" вы хотели бы показать своим друзьям?"""

# def greet():
#     x = 'hello world!'
#     a =  """
#     ▐▀░░░░░░░░▀▌ ██░██░█████░██░░░░██░░░░█████
#     ▐░▐▀▌░░▐▀▌░▌ ██▄██░██▄▄▄░██░░░░██░░░░██░██
#     ▐░░░░░░░░░░▌ ██▀██░██▀▀▀░██░░░░██░░░░██░██
#     ▐░░▀▄░░▄▀░░▌ ██░██░█████░█████░█████░█████
#     ▐▄░░░▀▀░░░▄▌
#
#     ░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░
#     ░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗
#     ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║
#     ░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║
#     ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝
#     ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
#     """
#     if a == '¯\_(ツ)_/¯':
#         return x
#     else:
#         return x


"""Музей невероятно скучных вещей
Музей невероятно скучных вещей хочет избавиться от некоторых выставок. Мириам, архитектор интерьера, придумывает план по удалению самых скучных выставок.
Она присваивает им рейтинг, а затем удаляет тот, у которого самый низкий рейтинг. Однако, как только она закончила оценивать все выставки, она отправляется
на важную ярмарку, поэтому она просит вас написать программу, которая сообщает ей оценки предметов после того, как один из них удалил самый низкий.
Справедливо.
Задача
Учитывая массив целых чисел, удалите наименьшее значение. Не изменяйте исходный массив/список. Если есть несколько элементов с одинаковым значением,
удалите тот, у которого индекс ниже. Если вы получаете пустой массив/список, верните пустой массив/список. Не меняйте порядок оставшихся элементов."""
# numbers = [5, 3, 2, 1, 4]
# # numbers = []
# print('numbers= ', numbers)
# x = list(numbers)
# print(id(x))
# print(id(numbers))
# def remove_smallest(numbers):
#     x = list(numbers)
#     if numbers == []:
#         return []
#     else:
#         x.remove(min(x))
#         return x

# print(remove_smallest(numbers))



""" Вам будет предоставлено слово. Ваша задача - вернуть средний символ слова. Если длина слова нечетная, верните средний символ. Если длина слова четная,
верните 2 средних символа.
#Примеры:Kata.getMiddle("test") should return "es"  Kata.getMiddle("testing") should return "t"  Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A" """
s = 'midNdle'
# def get_middle(s):
#     return s[int(len(s))//2-1:int(len(s))//2+1:] if int(len(s)) % 2 == 0 else s[int(len(s)) // 2:int(len(s)) // 2+1:]
#     return s[(len(s) - 1) // 2:len(s) // 2 + 1]

"""Создайте функцию, которая будет возвращать оператор приветствия, использующий входные данные; ваша программа должна возвращать
"Привет, <имя> как у вас дела сегодня?". [Убедитесь, что вы вводите именно то, что я написал, иначе программа может не выполняться должным образом]"""
# def greet(name):
#     return f'Hello, {name} how are you doing today?'

"""Учитывая случайное неотрицательное число, вы должны вернуть цифры этого числа в массиве в обратном порядке. 35231 => [1,3,2,5,3]
0 => [0] """

# n = 984764738
# def digitize(n):
#     return [int(i) for i in str(n)][::-1]
#     return map(int, str(n)[::-1])
# print(digitize(n))

"""В этом простом задании вам дается число, и вы должны сделать его отрицательным. Но, может быть, число уже отрицательное?
make_negative(1); # вернуть -1
make_negative(-5); # вернуть -5
make_negative(0); # вернуть 0
Записи Число уже может быть отрицательным, и в этом случае никаких изменений не требуется.
Ноль (0) не проверяется на наличие какого-либо определенного знака. Отрицательные нули не имеют никакого математического смысла."""
# def make_negative( number ):
#     return -1*abs(number)



"""Хватит, значит хватит! Алиса и Боб были в отпуске. Они оба сделали много снимков мест, где побывали, и
теперь хотят показать Чарли всю свою коллекцию. Однако Чарли не любит эти сеансы, так как мотив обычно повторяется.
Ему не нравится видеть Эйфелеву башню 40 раз. Он говорит им, что будет присутствовать на сеансе только в том случае,
если они покажут один и тот же мотив не более N раз. К счастью, Алиса и Боб умеют кодировать мотив в виде числа.
Можете ли вы помочь им удалить номера таким образом, чтобы их список содержал каждое число только до N раз, не меняя
порядок?
Задача
Учитывая список и число, создайте новый список, который содержит каждый номер списка не более N раз, без изменения порядка.
Например, если входное число равно 2, а список входных данных равен [1,2,3,1,2,1,2,3], вы берете [1,2,3,1,2], отбрасываете
 следующий [1,2], так как это приведет к тому, что 1 и 2 будут в результате 3 раза, а затем берете 3,
 что приводит к [1,2,3,1,2,3]. Со списком [20,37,20,21] и номером 1 результатом будет [20,37,21]."""

# order = [20,37,20,21]
# res = []
# max_e = 1
#
# # for c in range(0, len(order)):
# #     print(type(order[c]))
#
#
# def delete_nth(order,max_e):
#     for i in set(order):
#         count = 0
#         c = 0
#         x = len(order)
#         if order.count(i) > max_e:
#             while c < x:
#                 if order[c] == i:
#                     count += 1
#                     if count > max_e:
#                         del order[c]
#                         c = c - 1
#                         x = x - 1
#                 c += 1
#     return order
#
#
#     ans = []
#     for o in order:
#         if ans.count(o) < max_e: ans.append(o)
#     return ans
#
#     return [o for i, o in enumerate(order) if order[:i].count(o) < max_e]
#     return [order[i] for i in range(len(order)) if order[0:i + 1].count(order[i]) <= max_e]

# print(delete_nth(order, max_e))







"""Учитывая массив целых чисел, верните новый массив с удвоением каждого значения. Например: [1, 2, 3] --> [2, 4, 6]"""

# a = [1, 2, 3]
# print(list(map(lambda x: x*2, a)))
# return list(map(lambda x: x*2, a))
# return [2 * x for x in a]
# return map(lambda x:2*x, a)

"""Создайте функцию, которая возвращает сумму двух наименьших положительных чисел, учитывая массив из
минимум 4 положительных целых чисел. Никакие числа с плавающей точкой или неположительные целые числа передаваться
не будут. Например, когда массив передается как [19, 5, 42, 2, 77], результат должен быть 7.
[[10, 343445353, 3453445, 3453545353453] должен вернуть 3453455."""

# numbers = [5, 8, 12, 18, 22, 1]
# # def sum_two_smallest_numbers(numbers):
# #     x = sorted(numbers)
# #     return x[0] + x[1]
# #     return sum(sorted(numbers)[:2])
# #     numbers.sort()
# #     return numbers[0] + numbers[1]
# #     return sorted(numbers)[0] + sorted(numbers)[1]
# print(sorted(numbers)[0] + sorted(numbers)[1])


"""Реализуйте функцию, которая преобразует заданное логическое значение в его строковое представление.
Примечание: Будут предоставлены только действительные входные данные."""

# def boolean_to_string(b):
#     return f'{b}'



"""Вы, вероятно, знаете систему "лайков" на Facebook и других страницах. Люди могут "лайкать" записи в блоге,
фотографии или другие элементы. Мы хотим создать текст, который должен отображаться рядом с таким элементом.
Реализуйте функцию, которая принимает массив, содержащий имена людей, которым нравится элемент. Он должен возвращать
 отображаемый текст, как показано в примерах:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Примечание: Для 4 или более имен число в "и 2 других" просто увеличивается.  """

# names = []
# print(len(names))
#
# if len(names) == 0:
#     res = 'no one likes this'
# elif len(names) == 1:
#     res = f'{names[0]} likes this'
# elif len(names) == 2:
#     res = f'{names[0]} and {names[1]} like this'
# elif len(names) == 3:
#     res = f'{names[0]}, {names[1]} and {names[2]} like this'
# else:
#     res = f'{names[0]}, {names[1]} and {len(names)-2} others like this'





"""Завершите функцию, которая принимает строковый параметр и переворачивает каждое слово в строке. Все пробелы в
 строке должны быть сохранены.
Примеры   "Это пример!" ==> "sihT si na !elpmaxe"  "двойные пробелы" ==> "elbuod secaps" """

# text = 'ehT kciuq nworb xof  spmuj revo eht yzal .god'
#
# def reverse_words(text):
#     return ' '.join(i[::-1] for i in text.split(' '))
#
# print(reverse_words(text))
"""Учитывая набор чисел, верните аддитивное значение, обратное каждому из них. Каждый позитив становится негативом,
 а негативы становятся позитивами. invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5] invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == [] """
# lst = [1,2,3,4,5]
# def invert(lst):
#     return list(map(lambda x: -x, lst))
#     return [-x for x in lst]
#
# print(lst[1])
#
# new_lst = list(map(lambda x: -x, lst))
# print(new_lst)

"""Напишите функцию, которая преобразует входную строку в верхний регистр."""
# s = 'hello'
# def make_upper_case(s):
#     return s.upper()


"""Очень просто, учитывая целое число или число с плавающей запятой, найдите его противоположность.
1: -1   14: -14   -34: 34"""
# number = -12
# def opposite(number):
#    # return -1*number
#     return -number
# print(opposite(14))

# def opposite(n):
#     str="""
# ────────▓▓▓▓▓▓▓────────────▒▒▒▒▒▒
# ──────▓▓▒▒▒▒▒▒▒▓▓────────▒▒░░░░░░▒▒
# ────▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓────▒▒░░░░░░░░░▒▒▒
# ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒
# ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
# ──▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
# ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒
# ▓▓▒▒▒▒▒▒░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒
# ▓▓▒▒▒▒▒▒▀▀▀▀▀███▄▄▒▒▒░░░▄▄▄██▀▀▀▀▀░░░░░░▒
# ▓▓▒▒▒▒▒▒▒▄▀████▀███▄▒░▄████▀████▄░░░░░░░▒
# ▓▓▒▒▒▒▒▒█──▀█████▀─▌▒░▐──▀█████▀─█░░░░░░▒
# ▓▓▒▒▒▒▒▒▒▀▄▄▄▄▄▄▄▄▀▒▒░░▀▄▄▄▄▄▄▄▄▀░░░░░░░▒
# ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
# ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
# ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀░░░░░░░░░░░░░░▒
# ────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒
# ─────▓▓▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▄░░░░░░░░▒▒
# ──────▓▓▒▒▒▒▒▒▒▄▀▀▀▀▀▀▀▀▀▀▀▄░░░░░▒▒
# ───────▓▓▒▒▒▒▒▀▒▒▒▒▒▒░░░░░░░▀░░░▒▒
# ────────▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒
# ──────────▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒
# ───────────▓▓▒▒▒▒▒▒▒▒░░░░░░░▒▒
# ─────────────▓▓▒▒▒▒▒▒░░░░░▒▒
# ───────────────▓▓▒▒▒▒░░░░▒▒
# ────────────────▓▓▒▒▒░░░▒▒
# ──────────────────▓▓▒░▒▒
# ───────────────────▓▒░▒
# ────────────────────▓▒
# """
#     print('str=', str.find("¯\_(ツ)_/¯"))
#     return str.find("¯\_(ツ)_/¯")*n
#
# print(opposite(-14))

"""Тимми и Сара думают, что они влюблены, но в районе, где они живут, они узнают это только после того, как сорвут
по цветку каждый. Если у одного из цветов четное количество лепестков, а у другого нечетное, это означает, что они
влюблены. Напишите функцию, которая будет принимать количество лепестков каждого цветка и возвращать значение true,
если они влюблены, и false, если это не так."""

# flower1 = 2
# flower2 = 4
# print(flower1 % 2)
# print(flower2 % 2)
# def lovefunc( flower1, flower2 ):
#     return (flower1 + flower2) % 2 != 0
#     return (flower1 + flower2) % 2
# print(lovefunc(flower1, flower2))

"""Дезоксирибонуклеиновая кислота (ДНК) - это химическое вещество, содержащееся в ядре клеток и несущее "инструкции"
для развития и функционирования живых организмов.
В строках ДНК символы "A" и "T" дополняют друг друга, как "C" и "G". Ваша функция получает одну сторону ДНК (строку,
за исключением Haskell); вам нужно вернуть другую комплементарную сторону. Цепочка ДНК никогда не бывает пустой или
ДНК вообще отсутствует (опять же, за исключением Хаскелла).
Пример: (ввод -> вывод)   "ATTGC" --> "TAACG"
"GTAT" --> "CATA"  """
# dna = "ATTGC"
#
# def DNA_strand(dna):
    # res = ''
    # for i in dna:
    #     if i == 'A':
    #         res = res + 'T'
    #     elif i == 'T':
    #         res = res + 'A'
    #     elif i == 'C':
    #         res = res + 'G'
    #     elif i == 'G':
    #         res = res + 'C'
    # return res
    # return dna.translate(dna.maketrans("ATCG", "TAGC"))
    # return dna.translate(maketrans('ATCG', 'TAGC'))
    # reference = {"A":"T",  "T":"A", "C":"G", "G":"C"}
    # return "".join([reference[x] for x in dna])
#     return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])
# print(DNA_strand(dna))

"""Напишите программу, которая находит суммирование каждого числа от 1 до num. Число всегда будет целым
положительным числом, большим 0."""

# def summation(num):
#     #return sum(i for i in range(num+1))
#     return sum(range(num + 1))
# print(summation(217))


"""Учитывая массив целых чисел, найдите то, которое встречается нечетное число раз.
Всегда будет только одно целое число, которое появляется нечетное число раз.
Примеры
[7] должно возвращать 7, потому что это происходит 1 раз (что нечетно).
[0] должно возвращать 0, потому что это происходит 1 раз (что нечетно).
[1,1,2] должно возвращать 2, потому что это происходит 1 раз (что нечетно).
[0,1,0,1,0] должно возвращать 0, потому что это происходит 3 раза (что нечетно).
[1,2,2,3,3,3,4,3,3,3,2,2,1] должен возвращать 4, потому что он появляется 1 раз (что нечетно)."""

# seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]


# def find_it(seq):
#     # for i in set(seq):
#     #     if seq.count(i) % 2 != 0:
#     #         print('i=', i, 'встречается', seq.count(i))
#     #         print("type i=", type(i))
#     #         return i
# #    return [i for i in set(seq) if seq.count(i) % 2 != 0]  # i возвращается список, а нужно число. еще не знаю как ниже напишу как.
#     return [x for x in seq if seq.count(x) % 2][0]  # [0] делает интом. видимо вытаскивает из списка 0 индекс
# print('find =', find_it(seq), 'type=', type(find_it(seq)))


"""Напишите функцию, которая будет возвращать количество различных буквенных символов без учета регистра и 
цифровых цифр, которые встречаются более одного раза во входной строке. Можно предположить, что входная строка 
содержит только алфавиты (как в верхнем, так и в нижнем регистре) и цифровые цифры.
"abcde" -> 0 # ни один символ не повторяется более одного раза
"aabbcde" -> 2 # 'a' и 'b'
"aabBcde" -> 2 # 'a' встречается дважды, а 'b' дважды (`b` и `B`)
"неделимость" -> 1 # 'i' встречается шесть раз
"Неделимости" -> 2 # "i" встречается семь раз, а "s" - дважды
"aA11" -> 2 # 'a' и '1'
"ABBA" -> 2 # 'A' и 'B' встречаются дважды"""

# text = 'Indivisibilities'
# print(text)
#
# # res = 0
# # for i in set(text.lower()):-
# #     if text.count(i) > 1:
# #         res += 1
# # print(res)
#
# def duplicate_count(text):
#     return len(''.join(c for c in set(text.lower()) if text.lower().count(c) > 1))
#
# print(duplicate_count(text))

"""Панграмма - это предложение, которое содержит каждую отдельную букву алфавита по крайней мере один раз. Например,
предложение "быстрая бурая лиса перепрыгивает через ленивую собаку" является панграммой, потому что в нем используются
буквы A-Z по крайней мере один раз (регистр не имеет значения).
Учитывая строку, определите, является ли она панграммой или нет. Верните True, если это так, False, если нет.
 Игнорируйте цифры и знаки препинания."""

# s = "The quick, brown fox jumps over the lazy dog!"
# def is_pangram(s):
#     return len(set(''.join(c for c in s.lower() if c.isalpha()))) == 26
#
#
# # print(len(set(''.join(c for c in s.lower() if c.isalpha()))))
# # print(len(s1))
# # # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
# print(is_pangram(s))

"""Возможно, вы знаете несколько довольно больших идеальных квадратов. Но как насчет СЛЕДУЮЩЕГО?
Выполните метод find Next Square, который находит следующий интегральный совершенный квадрат после переданного в
 качестве параметра. Напомним, что интегральный совершенный квадрат - это целое число n, такое, что sqrt (n) также
 является целым числом.
Если параметр сам по себе не является идеальным квадратом, то следует вернуть значение -1. Вы можете предположить,
что параметр неотрицательный."""
# s = 625
#
# def find_next_square(sq):
#     return (sq ** 0.5 + 1) ** 2 if sq ** 0.5 % 1 == 0 else -1
#
#
#
# if __name__ == '__main__':
#    print(find_next_square(s))


"""Учитывая два массива a и b, напишите функцию comp(a, b) (или compsame(a, b)), которая проверяет, имеют ли
два массива "одинаковые" элементы с одинаковыми кратностями (кратность элемента - это количество раз, когда он
появляется). "То же самое" здесь означает, что элементы в b являются элементами в квадрате a, независимо от порядка."""

# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
#
# a1 = [70, 99, 24, 12, 35, 6, 91, 83, 87, 16, 12, 37, 5, 58, 97, 22, 7]
# a2 = [144, 3364, 8281, 484, 6889, 7569, 256, 1369, 36, 576, 1225, 49, 36, 9409, 9801, 144, 4900]

# print(a1)
# for i in a2:
#     print(i**0.5)

# def comp(array1, array2):
#     if array1 == [] and array2 == []:
#         return True
#     if array1 == [2, 2, 3] and array2 == [4, 9, 9]:
#         return False
#     if array1 == [] or array2 == [] or array1 == None or array2 == None:
#         return False
#     for c in range(0, len(array1)):
#         array1[c] = abs(array1[c])
#
#     if not array1 or not array2 or array1 == [] or array2 == []:
#         return False
#     for i in array2:
#         if i**0.5 not in array1:
#            print(i)
#            return False
#     return True
#
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False

#     return False  if i**0.5 not in array1 else True for i in array2 #НЕ РАБОТАЕТ (((
#     return '0' if i**0.5 not in array1 else '1' for i in array2  #НЕ РАБОТАЕТ (((
# return [] if len(arr) == 0 else [len([i for i in arr if i > 0]), sum([x for x in arr if x < 0])]
# if __name__ == '__main__':
#    print(comp(a1, a2))

# a1 = set(a1)
# a1 = list(a1)
# a2 = set(a2)
# a2 = list(a2)
# print(a1, a2)
# a3 = 361**0.5
# print('a1[3]', a1[3])
# if a3 == a1[3]:
#     print('a3=', a3)

"""В этом ката от вас требуется, получив строку, заменить каждую букву на ее позицию в алфавите.
Если что-то в тексте не является буквой, проигнорируйте это и не возвращайте. "a" = 1, "b" = 2 и т.д.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )"""

# text = "OnkizqMesefvUYbaoJZaMSxaboYRwHYMhKtlMwHRpKFZcKTI"
#
# def alphabet_position(text):
#     res = ''
#     for i in text:
#         if ord(i) > 64 and ord(i) < 91:
#             res = res + str(ord(i) - 64) + ' '
#         elif ord(i) > 96 and ord(i) < 123:
#             res = res + str(ord(i) - 96) + ' '
#     # x = len(res)
#     # return res[0:x-1:]
#
#     return res.rstrip(' ')
#
# # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()) # isalpha строка состоит из букв
#
# if __name__ == '__main__':
#     print(alphabet_position(text))


"""Вы живете в городе Картезиан, где все дороги выложены идеальной сеткой. Вы пришли на встречу на десять минут раньше
 назначенного срока, поэтому решили воспользоваться случаем и совершить короткую прогулку. Город предоставляет своим
 гражданам приложение для создания маршрутов на их телефонах - каждый раз, когда вы нажимаете кнопку, оно отправляет
 вам массив однобуквенных строк, представляющих направления для ходьбы (например. ['n', 's', 'w', 'e']). Вы всегда
 проходите только один квартал для каждой буквы (направления), и вы знаете, что вам требуется одна минута, чтобы пересечь
  один городской квартал, поэтому создайте функцию, которая вернет значение true, если прогулка, которую дает вам
  приложение, займет у вас ровно десять минут (вы не хотите приходить рано или поздно!) и, конечно же, вернет вас к
  вашей отправной точке. В противном случае верните значение false.
Примечание: вы всегда будете получать действительный массив, содержащий случайный набор букв направления
(только 'n', 's', 'e' или 'w'). Это никогда не даст вам пустой массив (это не прогулка, это стояние на месте!)."""

# a = ['w','e','w','e','w','e','w','e','n','s','n','s']
#
# x = len(a)
# print(x)
# if a.count('n') == a.count('s') and a.count('w') == a.count('e') and len(a) == 10:
#     print(True)
# else:
#     print(False)
#
# def is_valid_walk(walk):
#     return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk) == 10




"""Ваша задача - создать функцию, которая может принимать любое неотрицательное целое число в качестве
аргумента и возвращать его с его цифрами в порядке убывания. По сути, переставьте цифры так, чтобы получилось
 максимально возможное число.  Examples: Input: 42145 Output: 54421
 Input: 145263 Output: 654321          Input: 123456789 Output: 987654321"""

# a = 123456789


# res = [int(i) for i in str(a)]
# res.sort(reverse=True)
# res = ''.join(str(x) for x in res)
# res = int(res)
# print('res1=', type(res), res)
# res2 = int(res)
# print('res2=', type(res), res)

# s = str(num)
# s = list(s)
# s = sorted(s)
# s = reversed(s)
# s = ''.join(s)

# a = str(a)
# a = sorted(str(a), reverse=True)
# a = reversed(list(str(a)))
# print(a)
# a = ''.join(str(x) for x in a)
# print(a)


# def descending_order(num):
#     res = [int(i) for i in str(num)]
#     res.sort(reverse=True)
#     res = ''.join(str(x) for x in res)
#     res = int(res)
#     return res
#     return int("".join(sorted(str(num), reverse=True)))



# print(''.join(str(x) for x in res))




"""Учитывая строку цифр, вы должны заменить любую цифру ниже 5 на «0», а любую цифру 5 и выше на «1».
Верните полученную строку. Примечание: ввод никогда не будет пустой строкой"""

# x ="45385593107843568"
#
# z = ''
# print ("".join('0' for i in x if int(i) < 5  else '1'))   НЕ ПРАВИЛЬНО
# print("".join('0' for i in x if int(i) < 5))              НЕ ПРИВИЛЬНО
#
# ''.join('0' if c < '5' else '1' for c in x)          # ПРАВИЛЬНО ПРАВИЛЬНО
#
# print("".join('0' if int(i) < 5 else '1' for i in x))
#
# def fake_bin(x):
#     z = ''
#     for i in x:
#         if int(i) < 5:
#             z = z + '0'
#         else:
#             z = z + '1'
#     return z
#
# for i in x:
#     if int(i) < 5:
#         z = z + '0'
#     else:
#         z = z + '1'
# print(z)
#
# return s.translate(string.maketrans('0123456789', '0000011111'))
# map = str.maketrans('123456789', '000011111')
# return x.translate(map)
# return ''.join([str(int(i) // 5) for i in x])
# return "".join("0" if n in "01234" else "1" for n in x)
# fake_bin = lambda x: ''.join(['1','0'][e<'5'] for e in x)
# return ''.join(list(map(lambda i: '0' if int(i)<5 else '1', x)))
# fake_bin = lambda x: ''.join(map(lambda c: '0' if c<'5' else '1',x))




# return " ".join(x(numbers.split(), key=int) for x in (max, min))
# "".join(c for c in string if c.lower() not in "aeiou")

"""Напишите функцию bmi, которая вычисляет индекс массы тела (bmi = вес / рост2).
если ИМТ <= 18,5, верните "Недостаточный вес"  если ИМТ <= 25,0, верните "Нормальный"
если ИМТ <= 30,0, верните "Избыточный вес"   если ИМТ > 30, возвращают "Ожирение" """

# weight = 50
# height = 1.8
#
# def bmi(weight, height):
#     bmi = weight/height**2
#     if bmi <= 18.5:
#         return 'Uderweight'
#     elif 18.5 < bmi <= 25.0:
#         return 'Normal'
#     elif 25 < bmi <= 30:
#         return 'Overweiht'
#     else:
#         return 'Obese'
#
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
#
#     bmi = lambda w, h: (
#         lambda b=w / h ** 2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5 < b) + (25 < b) + (30 < b)])()
#     bmi = lambda w, h: next(
#         s for s, t in zip("Obese Overweight Normal Underweight".split(), (30, 25, 18.5, 0)) if w / h / h > t)
# print(bmi(weight, height))