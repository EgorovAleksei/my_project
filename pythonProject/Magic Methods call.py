
class MyInfoClass:
    def info(self):
        print(f'MyInfoClass  Информирую из функции {self}')

    def __call__(self, *args, **kwargs):
        self.info()

class MyOtherfoClass:
    def info_for_me(self):
        print(f'MyOtherfoClass   Информирую из {self}')

    def __call__(self, *args, **kwargs):
        self.info_for_me()

class NotMyOtherfoClass:
    def show_info(self):
        print(f'NotMyOtherfoClass   Информирую из {self}')

    def __call__(self, *args, **kwargs):
        self.show_info()

ex_1 = MyInfoClass()
ex_2 = MyOtherfoClass()
ex_3 = NotMyOtherfoClass()



# def info():
#     print(f'Информирую из info')
#
# def info_for_me():
#     print(f'Информирую из info_for_me')
#
# def show_info():
#     print(f'Информирую из show_info')

# notifications = [info, info_for_me, show_info, ex_1, ex_2, ex_3]
# notifications = [ex_1, ex_2, ex_3]
notifications = [MyInfoClass(), MyOtherfoClass(), NotMyOtherfoClass()]

for el in notifications:
    # print(el)
    el()


# info()
# print(info)
# print(info())
# info_for_me()
# show_info()