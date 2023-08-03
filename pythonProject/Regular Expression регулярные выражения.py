import re
string_re = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/xxxDCAC/DCAC/DCAC/DCAC/DCAC/DC SA'

# result_string_re = re.findall('DC', string_re)
# print(result_string_re)
#
# result_string_re = re.split('/',string_re, maxsplit=3)
# print(result_string_re)

# result_string_re = re.sub('A', 'D', string_re)
# result_string_re_sub_r = re.sub("[ACS]",'d', string_re)
# print(result_string_re)
# print(result_string_re_sub_r)
#( 'Длинна:', len(result_string_re))

# string_re = "ACC"
# result_string_re = re.fullmatch('A', string_re)


# print(result_string_re)

# s = "654+613 654+ ---- 6546f sdfsdf llmv KDJKFJ mvc?dskf +7-905-679-56-66"
# result = re.search(r'\d{,5}',s)
#
# print(result)

# s = 'Привет! Как дела? А у меня нормально.'
# result = re.findall(r'[бвкджзклмнпрстфхчшщ]\w+', s, re.I)

s = 'Еда, беду, победа, Еду домой'
result = re.findall(r'[еЕ]д[ау]', s)  # [а-я]  [а-яА-Я]  [a-zA-Z0-9]д[ау]
result = re.findall(r'[-0-9][0-9]', s) # ищет первый символ '-' или цифру, второй цифру
result = re.findall(r'[^0-9][0-9]', s) # ^0-9 ищет не цифры

print(result)


# if result:
#     print('result.group(): ', result.group())
# else:
#     print('Совпадений нет!')

# if result:
#     print('result.group(1): ', result.group(1))
# else:
#     print('Совпадений нет!')

# if result:
#     print('result.group(2): ', result.group(2))
# else:
#     print('Совпадений нет!')
#
# if result:
#     print('result.group(): ', result.groups())
# else:
#     print('Совпадений нет!')
