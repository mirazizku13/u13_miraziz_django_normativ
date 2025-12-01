class Shaxs:
    def __init__(self, name, familiya, yosh):
        self.name = name
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f'{self.name} {self.familiya} {self.yosh} yoshda'

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

class Talaba(Shaxs):
    def __init__(self, nomi, familiya, yosh, university):
        self.nomi = nomi
        self.familiya = familiya
        self.yosh = yosh
        self.university = university

    def get_info(self):
        return f'ismi: {self.nomi}\n familiyasi: {self.familiya}\n yoshi: {self.yosh}\n university: {self.university}'



def main():
    while True:
        print("=== TALABA BO'LIMI ===")
        print("1. Talaba haqida ma'lumot")
        print("2. Fanga yozilish")
        print("3. Fangni o‘chirish")
        print("4. Fanlar ro‘yxatini ko‘rish")
        print("5. Chiqish")

        a = int(input('nima qilasiz'))

        if a == 1:
            Talaba.get_info()
        elif a == 2:
            pass
        else:
            break
main()






















































#
# class Shaxs:
#     def __init__(self, ism, familiya, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, yosh, universitet):
#         super().__init__(ism, familiya, yosh)
#         self.universitet = universitet
#         self.fanlar = []  # bo‘sh ro‘yxat
#
#     def fanga_yozil(self, fan):
#         if isinstance(fan, Fan):
#             if fan not in self.fanlar:
#                 self.fanlar.append(fan)
#                 print(f"{self.ism} {fan.nomi} faniga yozildi.")
#             else:
#                 print(f"{fan.nomi} faniga allaqachon yozilgansiz.")
#         else:
#             print("Fan klassi obyekti emas!")
#
#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             print(f"{fan.nomi} fani o‘chirildi.")
#         else:
#             print("Siz bu fanga yozilmagansiz.")
#
#     def get_info(self):
#         fanlar_str = ', '.join([fan.nomi for fan in self.fanlar]) if self.fanlar else "Hozircha yo‘q"
#         return f"Talaba: {self.ism} {self.familiya}, {self.yosh} yoshda, {self.universitet}. Fanlar: {fanlar_str}"
#
# class Professor(Shaxs):
#     def __init__(self, ism, familiya, yosh, kafedra):
#         super().__init__(ism, familiya, yosh)
#         self.kafedra = kafedra
#
#     def get_info(self):
#         return f"Professor {self.ism} {self.familiya}, {self.kafedra} kafedrasi."
#
# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, familiya, yosh, username):
#         super().__init__(ism, familiya, yosh)
#         self.username = username
#
#     def get_info(self):
#         return f"Foydalanuvchi: {self.ism} {self.familiya} (login: {self.username})"
#
#
# class Admin(Foydalanuvchi):
#     def __init__(self, ism, familiya, yosh, username):
#         super().__init__(ism, familiya, yosh, username)
#         self.banned_users = []
#
#     def ban_user(self, foydalanuvchi):
#         if foydalanuvchi not in self.banned_users:
#             self.banned_users.append(foydalanuvchi)
#             print(f"Foydalanuvchi {foydalanuvchi.username} bloklandi.")
#         else:
#             print(f"{foydalanuvchi.username} allaqachon bloklangan.")
#
#     def get_info(self):
#         return f"Admin: {self.ism} {self.familiya} (login: {self.username})"
#
# matematika = Fan("Matematika")
# fizika = Fan("Fizika")
# tarix = Fan("Tarix")
# informatika = Fan("Informatika")
#
# fanlar = [matematika, fizika, tarix, informatika]
#
# talaba1 = Talaba("Ali", "Karimov", 20, "TATU")
#
# def main():
#     while True:
#         print("=== TALABA BO'LIMI ===\n1. Talaba haqida ma'lumot\n2. Fanga yozilish\n3. Fangni o‘chirish\n4. Fanlar ro‘yxatini ko‘rish\n5. Chiqish")
#         a = input("Tanlang: ")
#
#         if a == "1":
#             print(talaba1.get_info())
#
#         elif a == "2":
#             print("\nMavjud fanlar:")
#             for i, f in enumerate(fanlar, 1):
#                 print(f"{i}. {f.nomi}")
#             n = int(input("Qaysi fan? raqamini kiriting: "))
#             if 1 <= n <= len(fanlar):
#                 talaba1.fanga_yozil(fanlar[n - 1])
#             else:
#                 print("Xato tanlov!")
#
#         elif a == "3":
#             if not talaba1.fanlar:
#                 print("Sizda fan yo‘q.")
#                 continue
#             print("\nSiz yozilgan fanlar:")
#             for i, f in enumerate(talaba1.fanlar, 1):
#                 print(f"{i}. {f.nomi}")
#             n = int(input("Qaysi fanni o‘chirmoqchisiz? "))
#             if 1 <= n <= len(talaba1.fanlar):
#                 talaba1.remove_fan(talaba1.fanlar[n - 1])
#             else:
#                 print("Xato tanlov!")
#
#         elif a == "4":
#             print("Barcha fanlar:")
#             for f in fanlar:
#                 print("-", f.nomi)
#         else:
#             print("dastur tohtatildi")
#             break
#
# main()
