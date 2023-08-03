dict = {'яблоко': "красное", 'банан': "желтый", "лимон": 'желтый'}
for k in dict.keys():
    print('Ключи:',k)

for k in dict.values():
    print ('значения:', k)

for k in dict.items():
    print('Элементы:', k)

dict['банан'] = 'зеленый'
print(dict)

del(dict['банан'])
print(dict)

