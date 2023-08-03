from functools import reduce
"""перебирает строки в файле и делает из них числа"""
# with open('21-1a.txt') as f:
#     n = int(f.readline())
#
#     for i in range(n):
#         a, b = map(int, f.readli-ne().split())
''' считать файл mapp.txt. затем вывести числа в список, затем вывести
из них список нечетных'''
with open('mapp.txt') as file_map:

    a = list(map(int, file_map))
    print(a)
    x = list(filter(lambda x: (x % 2 == 1) , a))
    print(x)
# x = filter(lambda x: (x % 2 == 0), (2, 4, 5))

# def f(a, b):
#     return  a * b
#
# a = map(f, [2, 4, 5], [5, 6])
# print(list(a))
#
# a = map(lambda x: x + 15, (2, 4, 5))
# print(list(a))
#
# def z(y):
#     if y % 2 == 0:
#         return y
#
# y = filter(z, (2, 4, 5))
# print(list(y))
#
# x = filter(lambda x: (x % 2 == 0), (2, 4, 5))
# print(list(x))
#
# """ перемножает все числа друг с другом"""
# reduce_result = reduce(lambda a,b: a * b, (50, 57,  89, 12, 100))
# print(reduce_result)
#
# a_zip = [1, 2, 3, 4, 5, 6]
# b_zip = 'abcdef'
# result = zip(a_zip, b_zip)
# print(list(result))





# with open('21-1a.txt') as f2:
#     for line in f2:
#         print(line.strip())


"""пример readline and realines"""
# f1 = open('21-1a.txt','r')

# while True:
#     line = f1.readline()
#     if not line:
#         break
#     print(line.strip())

# line = f1.readlines()
#
# for line in line:
#     print(line)


# f1.close

