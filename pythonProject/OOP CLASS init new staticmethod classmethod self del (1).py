# class Person:
#     name = 'Ivan'
#     age = 30
#
#
# class Car:
#     model = 'BMW'
#     engine = 1.6
#
#
# print(getattr(Person, 'name'))
#
#
# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return (self.x, self.y)
#
#
# pt = Point()
# pt2 = Point()
# pt.set_coords(1, 2)
# pt2.set_coords(10, 20)
# print(pt.__dict__)  # {'x': 1, 'y': 2}
# print(pt2.__dict__)  # {'x': 10, 'y': 20}
#
# print(pt.get_coord())  # (1, 2)
# print(pt2.get_coord())  # (10, 20)
#
# f = getattr(pt, 'get_coord')
# print(f)  # <bound method Point.get_coord of <__main__.Point object at 0x000001493FB490D0>>
# print(f())  #  (1, 2)

# class Point:
#     color = 'red'
#     circle = 2
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление эксземпляра: ' + str(self))

# def set_coords(self, x, y):
#     self.x = x
#     self.y = y
#
# def get_coord(self):
#     return (self.x, self.y)


# pt = Point(1, 2)
# pt2 = Point(10, 20)
# print(pt)
# # pt.set_coords(1, 2)
# print(pt.__dict__)  # {'x': 1, 'y': 2}
# print(pt2.__dict__)  # {'x': 10, 'y': 20}
# pt3 = Point()
# print(pt3.__dict__)  # {'x': 0, 'y': 0}


# class Point:
#     color = 'red'
#     circle = 2
#
#     def __new__(cls, *args, **kwargs):
#         print('вызов __new__ для ', cls)
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# print(pt)

# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __del__(self):
#         DataBase.__instance = None
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")
#
#     def close(self):
#         print('закрытие соединения с БД')
#
#     def read(self):
#         return 'Данные с БД'
#
#     def write(self, data):
#         print(f'запись в БД {data}')
#
#
# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)
# print(id(db), id(db2))
# print(db2.__dict__)
# db.connect()
# db2.connect()

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
#
#
# v = Vector(1, 2)
# res = v.get_coord()
# res1 = Vector.get_coord(v)
# print(res) # (1, 2)
# print('res1', res1) #res1 (1, 2)
#
# print(Vector.validate(5)) # True
#
# print(v.validate(4))  # True

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x,y):
        return x*x + y*y

v = Vector(10, 20)

print(Vector.norm2(5, 6)) # 61

