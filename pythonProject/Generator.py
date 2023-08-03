
# s = []
# for i in range(1, 21):
#     if i % 5 == 0:
#         s.append(i)
# print (s)
#
#
# s1 = [i**3 for i in range(1, 21) if i % 5 ==0]
# print(s1)
# print(sum(s1))
# print (sum([i**3 for i in range(1, 21) if i % 5 ==0]))
#
#
# s2 = []
# for i in range (1, 21):
#     for j in range (1, 51):
#         s2.append((i,j))
# print(s2)
#
# s3 = [(i,j) for i in range(1,21) for j in range(1,51)]
# print(s3)
#
# """создадим список от -10 до 10 и заполним если отрицательный их кубами если
# положительный их квадратами"""
#
# s4 = []
# for i in range (-10, 11):
#     if i < 0:
#         s4.append(i ** 3)
#     else:
#         s4.append(i ** 2)
#
#
# print('s4=', s4)
#
# s5 = [i ** 2 if i > 0 else i ** 3 for i in range (-10,11) if i % 2 == 0]
# s5 = [
#     i ** 2
#     if i > 0
#     else i ** 3
#     for i in range (-10,11)
#     if i % 2 == 0
# ]
# print('s5=', s5)


s6 = [7, 8, 8, 9, -10, -10 ]
set_set = {i for i in s6}
print(set_set)
print(type(set_set))
dictionary = {i: i ** 10 for i in s6}

dictionary1 = {
    i: i **10
    for i in s6
}
print(dictionary)





