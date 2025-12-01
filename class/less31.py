# from multiprocessing.pool import worker
#
#
# class Student:
#     def __init__(self, name, age, course, unv, city = 'tashkent'):
#         self.name = name
#         self.age = age
#         self.course = course
#         self.unv = unv
#         self.city = city
#
#     def get_info(self):
#         return f'Talaba nomi {self.name}, yoshi {self.age}, course {self.course}, univer {self.unv}, city {self.city}'
#
# name = input('name: ')
# age = int(input("age: "))
# course = int(input("course: "))
# unv = input("unv: ")
# city = input("city")
# s2 = Student(name,age,course,unv,city)
# s1 = Student('ALi', 20, 2, 'tatu', 'buhara')
# print(s1.get_info())
# print(s2.get_info())
# s1.age = 25
# print(s1.get_info())
# print(s2.get_info())
#
#
# class Work(Student):
#     def __init__(self, name, age, course, unv, city = 'tashkent', work = 'ish siz'):
#         super().__init__(name, age, course, unv, city)
#         self.work = work
#
#     def get_info(self):
#         return f"ishchi {self.name} yoshi {self.age} {self.city}li universiteti {self.unv} - {self.course} kursni tugatgan hozirgi ishi {self.work}"

# worker = ('ALi', 20, 2, 'tatu', 'buhara')
# print(worker.get_info())

sonlar = [12,23,31,42]
total = 0
kopayma = 1
for i in sonlar:
    total +=i
    kopayma *=i
print(sum(sonlar),"sum bilan")
print(total)
print(kopayma)
