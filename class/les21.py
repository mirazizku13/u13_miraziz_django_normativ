# class Avto:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#         self.km = 0
#
#
#     def get_km(self):
#         return self.km
#
#     def update_km(self, km):
#         if km > 0:
#             self.km += km
#         else:
#             print('manfiy qiymat mumkin emas')
#
# avto = Avto("Avto", 'GM')
#
#
# avto.update_km(-10)
# print(avto.km)





#
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password
#         self. _balance = 0
#     def set_password(self, password):
#         self.__password = password
#
#
#
# class Doctor(User):
#     def __init__(self, username, password, patients):
#         super().__init__(username, password)
#         self._patients = []
#
#     # def get_password(self):
#     #     return self.__password
#
#      def get_bslsnce(self):
#         return self._balance
#
# user = User("Rustam", "12221")
# doctor = Doctor("Rusa", "12", [])
# # print(doctor.get_password())
#
# print(doctor.get_bslsnce())
# print(doctor.bslsnce())






















from abc import ABC, abstractmethod
#
# class ATM(ABC):
#     @abstractmethod
#     def enter_pin(self, password):
#
#         pass
#
#     @abstractmethod
#     def get_balance(self):
#         pass
#
#     @abstractmethod
#     def withdraw_mony(self, mony):
#         pass
#
# class NBUATM(ATM):
#     def enter_pin(self, password):
#         print('pin kirit')
#
#     def get_balance(self):
#         print('balance')
#
#     def withdraw_mony(self, mony):
#         print(f'{mony} yechib olindi')









# atm = NBUATM()
# print(atm)
















# class LibraryItem(ABC):
#     def __init__(self, title, upc, subject):
#         self.title = title
#         self.upc = upc
#         self.subject = subject
#
#     @abstractmethod
#     def locate(self):
#         pass
#
# class Author:
#     def __init__(self, full_name, bio):
#         self.full_name = full_name
#         self.bio = bio
#
#
#
# class Book(LibraryItem):
#     def __init__(self, title, upc, subject, author, year, genre, dds_number, isbn):
#         super().__init__(title, upc, subject)
#         self.author = author
#         self.year = year
#         self.genre = genre
#         self.dds_number = dds_number
#         self.isbn = isbn
#
#     def locate(self):
#         return f'dds raqami: {self.dds_number}'
#
#
# class Magazine(LibraryItem):
#     def __init__(self, title, upc, subject, volume, issue):
#         super().__init__(title, upc, subject)
#         self.volume = volume
#         self.issue = issue
#
#     def locate(self):
#         return f'Volume: {self.volume}, Issue: {self.issue}'
#
# class DVD(LibraryItem):
#     def __init__(self, title, upc, subject, actors, director, genre):
#         super().__init__(title, upc, subject)
#         self.actors = actors
#         self.director = director
#         self.genre = genre
#
#     def locate(self):
#         return self.actors
#
# class CD(LibraryItem):
#     def __init__(self, title, upc, subject, artist):
#         super().__init__(title, upc, subject)
#         self.artist = artist
#
#     def locate(self):
#         return self.artist
#
# class Catalog:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#
#     def add_item(self, item):
#         if isinstance(item, LibraryItem):
#             self.items.append(item)
#         else:
#             print('Error')
#
#     def get_item(self):
#         if not self.items:
#             print('katalog bo`sh')
#         else:
#             return self.items
#
#     def search(self):
#         result = []
#         for item in self.items:
#             if keyword.lower() in item.title.lower() or keyword.lower() in item.subject.lower():
#                 result.append(item)
#         return result
# c1 = Catalog('1-katalog')
# def main():
#     while True:
#         print('\n==================================')
#         print("========   KATALOG MENU   ========")
#         print('==================================')
#         print("1. Kitoblar ro‘yxati")
#         print("2. Yangi kitob qo‘shish")
#         print("3. Kitobni qidirish")
#         print("4. Chiqish")
#
#         choice = input("Nima qilasiz: ")
#
#         if choice == '1':
#             print('===============================================')
#             print("========katalogdagi barcha item royhati========")
#             print('===============================================')
#             c1.get_item()
#         elif choice == '2':
#             print('============================')
#             print("========yangi item qoshish========")
#             print('============================')
#             print('Nima qoshasiz\n1.Book\n2.magazine\n3.DVD\n4.CD')
#             a = int(input("Nima qilasiz: "))
#             if a == 1:
#                 print('===========================')
#                 print('========   Book   =========')
#                 print('===========================')
#
#             elif a == 2:
#                 print('===========================')
#                 print('======== magazine =========')
#                 print('===========================')
#
#             elif a == 3:
#                 print('============================')
#                 print('========    DVD    =========')
#                 print('============================')
#
#             elif a == 4:
#                 print('===========================')
#                 print('========    CD    =========')
#                 print('===========================')
#
#         elif choice == '3':
#             print('==================================')
#             print("======== itemlarni ko`rish =======")
#             print('==================================')
#         elif choice == '4':
#             print('============================')
#             print("========    Exit    ========")
#             print('============================')
#             break
#
# main()
















#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.books.append(book)
#         else:
#             print('❌ Book klassining obyekti emas!')
#
#     def get_books(self):
#         if not self.books:
#             return "📚 Katalogda hali kitob yo‘q!"
#         result = ""
#         for i in self.books:
#             result += f"{i.name}, {i.author.full_name}, {i.year}, {i.genre}, {i.dds_number}, {i.isbn}\n"
#         return result
#
#     def search_book(self, name):
#         for i in self.books:
#             if i.name.lower() == name.lower():
#                 print(f"✅ {i.name} kitobi mavjud. DDS raqami: {i.dds_number}")
#                 return i
#         print(f"❌ {name} kitobi topilmadi.")
#         return None
#
#
# # ---- Asosiy dastur ----
# author1 = Author('Ibn Xaldun', "Arab tarixchisi va faylasufi.")
# book1 = Book('Muqqadima', author1, 1389, 'Siyosat', 2034, 1232323)
# book2 = Book('Muqqadima 2', author1, 1399, 'Siyosat', 2035, 1232123)
#
# c1 = Catalog('1-katalog')
# c1.add_book(book1)
# c1.add_book(book2)
#
#
# def main():
#     while True:
#         print("\n========== KATALOG MENU ==========")
#         print("1. Kitoblar ro‘yxati")
#         print("2. Yangi kitob qo‘shish")
#         print("3. Kitobni qidirish")
#         print("4. Chiqish")
#
#         choice = input("Nima qilasiz: ")
#
#         if choice == "1":
#             print("\n--- Kitoblar ro‘yxati ---")
#             print(c1.get_books())
#
#         elif choice == "2":
#             print("\n--- Yangi kitob qo‘shish ---")
#             name = input("Kitob nomi: ")
#             author_name = input("Muallif ismi: ")
#             year = int(input("Yili: "))
#             genre = input("Janri: ")
#             dds = int(input("DDS raqami: "))
#             isbn = input("ISBN raqami: ")
#
#             new_author = Author(author_name, "Bio yo‘q")
#             new_book = Book(name, new_author, year, genre, dds, isbn)
#             c1.add_book(new_book)
#             print(f"✅ '{name}' kitobi muvaffaqiyatli qo‘shildi!")
#
#         elif choice == "3":
#             name = input("Qidirayotgan kitob nomi: ")
#             c1.search_book(name)
#
#         elif choice == "4":
#             print("👋 Dasturdan chiqildi. Xayr!")
#             break
#
#         else:
#             print("❌ Noto‘g‘ri tanlov! 1-4 oralig‘ida tanlang.")
#
#
# main()















































class LibraryItem(ABC):
    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject

    @abstractmethod
    def locate(self):
        pass


class Author:
    def __init__(self, full_name, bio):
        self.full_name = full_name
        self.bio = bio


class Book(LibraryItem):
    def __init__(self, title, upc, subject, author, year, genre, dds_number, isbn):
        super().__init__(title, upc, subject)
        self.author = author
        self.year = year
        self.genre = genre
        self.dds_number = dds_number
        self.isbn = isbn

    def locate(self):
        return f'DDS raqami: {self.dds_number}'

    def __str__(self):
        return f"📘 {self.title} — {self.author.full_name} ({self.year})"


class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.issue = issue

    def locate(self):
        return f'Volume: {self.volume}, Issue: {self.issue}'

    def __str__(self):
        return f"📰 {self.title} — Vol.{self.volume}, Issue {self.issue}"


class DVD(LibraryItem):
    def __init__(self, title, upc, subject, actors, director, genre):
        super().__init__(title, upc, subject)
        self.actors = actors
        self.director = director
        self.genre = genre

    def locate(self):
        return f"Aktorlar: {', '.join(self.actors)}"

    def __str__(self):
        return f"🎬 {self.title} — Rejissor: {self.director}"


class CD(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)
        self.artist = artist

    def locate(self):
        return f"Ijrochi: {self.artist}"

    def __str__(self):
        return f"{self.title} — {self.artist}"


class Catalog:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.items.append(item)
            print(f"{item.title} katalogga qo‘shildi.")
        else:
            print('Error: faqat LibraryItem obyektini qo‘shish mumkin!')

    def get_item(self):
        if not self.items:
            print('📭 Katalog bo‘sh!')
        else:
            for item in self.items:
                print(item)

    def search(self, keyword):
        result = []
        for item in self.items:
            if keyword.lower() in item.title.lower() or keyword.lower() in item.subject.lower():
                result.append(item)
        return result


c1 = Catalog('1-katalog')

def main():
    while True:
        print('\n==================================')
        print("========   KATALOG MENU   ========")
        print('==================================')
        print("1. Itemlar ro‘yxati")
        print("2. Yangi item qo‘shish")
        print("3. Itemni qidirish")
        print("4. Chiqish")

        choice = input("Tanlov: ")

        if choice == '1':
            print('\nKatalogdagi barcha itemlar:')
            c1.get_item()

        elif choice == '2':
            print('\nQanday item qo‘shmoqchisiz?')
            print('1. Book\n2. Magazine\n3. DVD\n4. CD')
            a = input("Tanlang (1-4): ")


            if a == '1' or a.lower() == 'book':
                title = input("Sarlavha: ")
                upc = input("UPC kodi: ")
                subject = input("Mavzu: ")
                author_name = input("Muallif ismi: ")
                author_bio = input("Muallif haqida: ")
                author = Author(author_name, author_bio)
                year = input("Yil: ")
                genre = input("Janr: ")
                dds = input("DDS raqami: ")
                isbn = input("ISBN: ")
                b = Book(title, upc, subject, author, year, genre, dds, isbn)
                c1.add_item(b)


            elif a == '2' or a.lower() == 'magazine':
                title = input("Sarlavha: ")
                upc = input("UPC kodi: ")
                subject = input("Mavzu: ")
                volume = input("Volume: ")
                issue = input("Issue: ")
                m = Magazine(title, upc, subject, volume, issue)
                c1.add_item(m)


            elif a == '3' or a.lower() == 'dvd':
                title = input("Sarlavha: ")
                upc = input("UPC kodi: ")
                subject = input("Mavzu: ")
                actors = input("Aktorlar (vergul bilan): ").split(',')
                director = input("Rejissor: ")
                genre = input("Janr: ")
                d = DVD(title, upc, subject, actors, director, genre)
                c1.add_item(d)


            elif a == '4' or a.lower() == 'cd':
                title = input("Sarlavha: ")
                upc = input("UPC kodi: ")
                subject = input("Mavzu: ")
                artist = input("Ijrochi: ")
                cd = CD(title, upc, subject, artist)
                c1.add_item(cd)

            else:
                print("Noto‘g‘ri tanlov!")

        elif choice == '3':

            keyword = input("\nQidirilayotgan so‘zni kiriting: ")
            results = c1.search(keyword)
            if results:
                print(f"\n{len(results)} ta natija topildi:")
                for r in results:
                    print(r)
            else:
                print("Hech narsa topilmadi.")

        elif choice == '4' or choice == '':
            print('\nDasturni yakunlash.')
            print('Hayir salomat bo`ling!')
            break

        else:
            print("Noto‘g‘ri tanlov! Faqat 1,2,3,4.")


main()
