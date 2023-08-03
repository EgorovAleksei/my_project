


"""
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems.
It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from
DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic
acid Uracil ('U').
Create a function which translates a given DNA string into RNA.
For example: "GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed
to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
"""

# def dna_to_rna(dna):
#     result = ''
#     for i in range(0, len(dna)):  =  for i in dna
#         if dna[i] == 'T':
#             result = result + 'U'
#         else:
#             result = result + dna[i]
#     return result

# def dna_to_rna(dna):
#     return dna.replace('T', 'U')
#     return "".join(["U" if c=="T" else c for c in dna])

# def dna_to_rna(dna):
#     RNA= ""
#     i = 0
#     for i in dna:
#         if i == "T":
#             RNA = RNA + "U"
#         else:
#             RNA = RNA + i
#     return RNA
#
# if __name__ == '__main__':
#     print(dna_to_rna('GACCGCCGCC'))





"""
We need a function that can transform a number (integer) into a string.
What ways of achieving this do you know?
Нам нужна функция, которая может преобразовать число (integer) в строку.
Какие способы достижения этого вы знаете?
Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
number_to_string(1-2), '-1'
"""
# num = 1 + 2
# def number_to_string(num):
#     return str(num)
#
#
# print(type(number_to_string(num)))
# print(number_to_string(num))






"""Century From Year"""
"""Первое столетие охватывает период с 1 года по 100 год включительно, 
второе столетие - с 101 года по 200 год включительно и т.д.
Задача
Учитывая год, верните столетие, в котором он находится."""

# x = 1901
# y = x // 100
# z = y * 100
# if x <= z:
#     print(x, ' century', y)
# else:
#     print('century', y +1 )
# print('y =', y, 'z=',z )
# year = x
#
# def century(year):
#     return year // 100 if year <= year // 100  * 100 else year // 100 + 1
#     return (year + 99) // 100

# print(century(year))

# seq = [78, 117, 110, 99, 104, 117, 107, 115]
# elem = 79
# def check(seq, elem):
#     return True if elem in seq else False
#     return elem in seq
# print(check(seq, elem))



# class_points = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# your_points = 69
# # [12, 23, 34, 45, 56, 67, 78, 89, 90], 69
#
# print(sum(class_points))
# print(len(class_points))
# x = sum(class_points) / len(class_points)
#
# print(class_points)
# print(type(your_points))
#
# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)
#    # pass
#    # return True if sum(class_points)/len(class_points) < your_points else False
#
# print(better_than_average(class_points, your_points))






# a = True
# print([2, 'vfdd'][str])
# print(a)
# match a:
#     case True:
#         a = 'Yes'
#         print(a)
#     case [False]:
#         print('no')


# def bool_to_word(boolean):
#     match boolean:
#         case True:
#             return 'Yes'
#         case False:
#             return 'No'
#
# def bool_to_word(bool):
#     return ['No', 'Yes'][bool]
#
# bool_to_word = ['No','Yes'].__getitem__
