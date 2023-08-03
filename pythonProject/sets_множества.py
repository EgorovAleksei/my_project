sets_number = {1, 2, 3, 4, 5, 6, 7}
sets_number2 = {2, 6, 54, 42, 3}

# for i in sets_number:
#     print(i)
# print(58 in sets_number)
# print(type(3 in sets_number))

# sets_number.add(58)
# sets_number.discard(68)
# try:
#     sets_number.remove(78)
# except KeyError:
#     print('there is no such nubmer')
# print(sets_number)
#
# sets_number.pop()
# print(sets_number)
#
# sets_number.clear()
# print(sets_number)

# sets_number3 = sets_number.union(sets_number2)
# sets_number3 = sets_number | sets_number2 # вместо union
# sets_number3 = sets_number.intersection(sets_number2) # вносим повторяющиеся
# sets_number3 = sets_number & sets_number2 # & вместо intersection

# sets_number3 = sets_number - sets_number2 # ищет уникальные 1 множестве
# sets_number3 = sets_number2 - sets_number # ищет уникальные во 2 множестве сете

# sets_number3 = sets_number2.copy()
sets_number_frozenset = frozenset({1, 2, 3, 4, 5, 6, 7})
# sets_number_frozenset.add(8)
sets_number.add(8)
print(sets_number)
print(sets_number_frozenset)
