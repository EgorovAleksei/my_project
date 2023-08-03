import itertools
from string import digits, punctuation, ascii_letters
import win32com.client as client



from datetime import datetime
import time

# symbols = digits + punctuation + ascii_letters
# print(symbols)

def brute_excel_doc():
    try:
        password_length = input('Введите длину пароля например 3 - 7:')
        password_length = [int(item) for item in password_length.split('-')]
#        print('password_length', password_length)
    except:
        print('Проверьте введенные данные')

    print('Если пароль содержит только цифры, введите: 1\nЕсли пароль содержит только буквы введите 2\n'
          'Если пароль содержит цифры и буквы введите: 3\nЕсли пароль содержит всё введите 4:')
    try:
        choice = int(input(': '))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = 'Не то ввел'
        print(possible_symbols)
    except:
        print(possible_symbols)

    #brute excel doc
    start_timestamp = time.time()
    print(f"Started at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
    count = 0
    for pass_length in range(password_length[0], password_length[1]+1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = ''.join(password)
          #  print(password)
            open_doc = client.Dispatch("Excel.Application")
            count += 1
            try:
                open_doc.Workbooks.Open(
#                    r"C:\1234.xlsx",
                    r"E:\gh31\Бух учет\! Касса с 01.10.xlsx",
                    False,
                    True,
                    None,
                    Password=password
                )
                time.sleep(0.1)
                print(f'Finished at - {datetime.utcfromtimestamp(time.time()).strftime("%H:%M:%S")}')
                print(f'Password cracking time - {time.time() - start_timestamp}')
                return f'Attempt #{count} Password is: {password}'
            except:
                print(f'Attemp #{count} Incorrect{password}')



def main():
    print(brute_excel_doc())

if __name__ == '__main__':
    main()
