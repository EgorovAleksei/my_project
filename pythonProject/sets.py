rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indogo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56, 3, 3, 3]
text_tuple = ('sfds', 'aafg', 'dfsd', 'hi', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
set_from_list.add(777)
set_from_tuple.add('hello')

print(set_from_list)
print(set_from_tuple)

# set_from_list.pop()
# print(set_from_list)

y = set_from_list.remove(43)
print('y', y)

z = set_from_list.discard(3)
print(z)