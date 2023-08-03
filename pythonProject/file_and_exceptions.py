# file = open('1.txt',"w")
# file.write('Привет!!! Hello, World!!')
# file.close()


# file = open('1.txt', 'r')
# print(file.read())
# file.close()

# with open('1.txt', 'a') as f:
#     f.write('Белгород '+'\n')
# print(f)


try:

    b = int(input('a: '))
    a = int(input('b: '))
    print(a / b)
except ValueError:
    print('Надо вводить число')
except ZeroDivisionError:
    print('На 0 делить нельзя!')

