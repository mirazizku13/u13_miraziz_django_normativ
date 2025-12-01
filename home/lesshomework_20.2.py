# class Student:
#     def __init__(self, name, age, jinsi, country, course, fak):
#         self.name = name
#         self.age = age
#         self.jinsi = jinsi
#         self.country = country
#         self.course = course
#         self.fak = fak
#         self.fanlar = []
#
#
#     def get_info(self):
#         return f"Student ismi: {self.name} yoshi: {self.age} jinsi: {self.jinsi} kursi: {self.course} fakulteti: {self.fak} fanlar: {self.fanlar}"
#
# class Fanlar(Student):
#     def __init__(self, name, age, jinsi, country, course, fak):
#         super().__init__(self, name, age,jinsi, country, course, fak)
#
#     def get_info_fanlar(self):
#         return f"fanlar: {self.fanlar}"
#
#
#     def add_fanlar(self, fanlar):
#         self.fanlar.append(fanlar)
#
#     def remove_fanlar(self, fanlar):
#         self.fanlar.remove(fanlar)
#
#     def get_info_student(self):
#         return f"Student ismi: {self.name} fanlari {self.fanlar} "
#
#
#
# studentlar = []
#
#
# def admin():
#     print("admin menu")
#     ism = input("admin name: ")
#
#     a = int(input("1.studentlarni ko`rish\n2.studentga fan qoshish\nstudentdan fan olib tashlash\nnima qilasiz: "))
#     if a == 1:
#         print(f"admin {ism}\n studentlar: {Student.get_info()}")
#     elif a == 2:
#         fan = input("studentni fani: (matem) ")
#         Fanlar.add_fanlar(fan)
#         Fanlar.get_info_fanlar()
#
# def student():
#     print("student menu")
#     ism = input("student name: ")
#     age = int(input("student age: "))
#     jinsi = input("student jinsi: ")
#     country = input("student country: ")
#     course = input("student course: ")
#
#     s1 = Student(ism, age, jinsi, country, course)
#     print(s1.get_info())
#
# a = int(input("1.adminga kirish\n2.studentga kirish"))
# if a == 1:
#       admin_user = "adminadmin"
#       admin_pass = "admin2"
#       b = (input("admin username: "))
#       b2 = (input("admin password: "))
#       if b == admin_user and b2 == admin_pass:
#             print("adminga hush kelibsiz")
#             admin()
#       else:
#             print("login or password incorrect")
#
# elif a == 2:
#     print(f"{Student.name} salom")
#     student()
#
#
#










#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
# class Sotuvchi(Person):
#     def __init__(self, name, age, type_):
#         super().__init__(name, age)
#         self.type_ = type_
# class Student(Person):
#     def __init__(self, name, age, jinsi, country, course, fak):
#         super().__init__(name, age)
#         self.jinsi = jinsi
#         self.country = country
#         self.course = course
#         self.fak = fak
#         self.fanlar = []
#
#     def fanga_yozil(self, fan):
#         if isinstance(fan, Fan):
#             self.fanlar.append(fan)
#         else:
#             print('xato')
#
#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             print('fan topilmadi')
#
# class Fan:
#     def __init__(self, name):
#         self.name = name
#
#
#
#
# matimatika = Fan('Matematika')
# fizika = Fan('Fizika')





























































class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Ism: {self.name}, Yosh: {self.age}"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __repr__(self):
        return self.nomi

class Student(Person):
    def __init__(self, name, age, jinsi, country, course, fak):
        super().__init__(name, age)
        self.jinsi = jinsi
        self.country = country
        self.course = course
        self.fak = fak
        self.fanlar = []  # bo‘sh ro‘yxat

    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            self.fanlar.append(fan)
            print(f"{self.name} {fan.nomi} faniga yozildi.")
        else:
            print("Xato: faqat Fan obyektini kiriting!")

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan.nomi} fani ro‘yxatdan olib tashlandi.")
        else:
            print("Siz bu fanga yozilmagansiz!")

    def get_info(self):
        fanlar_str = ', '.join([f.nomi for f in self.fanlar]) if self.fanlar else "Hali fan yo‘q"
        return f"Talaba: {self.name}, Yosh: {self.age}, Fanlar: {fanlar_str}"


class Sotuvchi(Person):
    def __init__(self, name, age, type_):
        super().__init__(name, age)
        self.type_ = type_

    def get_info(self):
        return f"Sotuvchi: {self.name}, Yosh: {self.age}, Turi: {self.type_}"


class Foydalanuvchi(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {self.name}, Email: {self.email}"


class Admin(Foydalanuvchi):
    def __init__(self, name, age, email, role="Admin"):
        super().__init__(name, age, email)
        self.role = role

    def ban_user(self, user):
        print(f"Foydalanuvchi {user.name} bloklandi!")

    def get_info(self):
        return f"Admin: {self.name}, Rol: {self.role}, Email: {self.email}"


# ==== Sinov uchun kod ====

matematika = Fan("Matematika")
fizika = Fan("Fizika")

talaba1 = Student("Ali", 20, "Erkak", "Uzbekistan", 2, "Informatika")
talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)
print(talaba1.get_info())

talaba1.remove_fan(matematika)
print(talaba1.get_info())

admin1 = Admin("Rustam", 30, "rustam@example.com")
user1 = Foydalanuvchi("Dilshod", 25, "dilshod@gmail.com")
admin1.ban_user(user1)
