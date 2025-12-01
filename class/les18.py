class Student:
    def __init__(self, name, age, course, unv):
        self.name = name
        self.age = age
        self.course = course
        self.unv = unv

    def get_info(self):
        return f'Talaba nomi {self.name}, yoshi {self.age}, course {self.course}, univer {self.unv}'


s1 = Student('ALi', 20, 2, 'tatu')
# s1.get_info()
# # print(s1.name, s1.age, s1.course, s1.unv)
# # print(s1.name)
# #
# # a = 12
# # print(type(a))




class User:
    def __init__(self, name, nik_name, email):
        self.name = name
        self.nik_name = nik_name
        self.email = email

    def get_info(self):
        return f'ismi {self.name} foydalanovchi ismi {self.nik_name} emaili {self.email}'


u1 = User('miraziz', 'mirazizk', 'miraziz2008@yandex.com')
print(u1.name, u1.nik_name, u1.email)
print(u1.get_info())
