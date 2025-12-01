
class Author:
     def __init__(self, full_name, bio):
         self.full_name = full_name
         self.bio = bio


class Book:
     def __init__(self,name, author, year, genre, dds_number, isbn):
         self.name = name
         self.author = author
         self.year = year
         self.genre = genre
         self.dds_number = dds_number
         self.isbn = isbn



class Catalog:
     def __init__(self,name):
         self.name = name
         self.books = []
author1 = Author("Ibn Xaldun", """bn Xaldun Abduraxman Abu Zayd Ibn Muhammad (1332-yil 27-may, Tunis – 1406-yil 17-mart, Qohira) – arab tarixchisi va faylasufi. Ibn Rushdning izdoshi. 1349–1375-yillarda Tunis, Fes, Gʻarnota, Bujjoya (Jazoirda) hukmdorlari saroyida yuqori lavozimlarda ishlagan. 1382-yil Misrga kelib, mudarrislik qilgan, umrining oxirida molikiylar mazhabi qozisi boʻlgan.""")

book1 = Book("Muqqadima", "ibn xaldun", "1389", 'siyosat', 2034, 1232846512)
c1 = Catalog("1-catalog")
c1.books.append(book1)

print(c1.books)


class Author:
     def __init__(self, full_name, bio):
         self.full_name = full_name
         self.bio = bio


class Book:
     def __init__(self, name, author, year, genre, dds_number, isbn):
         self.name = name
         self.author = author
         self.year = year
         self.genre = genre
         self.dds_number = dds_number
         self.isbn = isbn


class Catalog:
     def __init__(self, name):
         self.name = name
         self.books = []

     def add_book(self, book):
         if isinstance(book, Book):
             self.books.append(book)
         else:
             print('Book classini obiyeti emas')

     def get_books(self):
         for i in self.books:
             return f"{i.name}, {i.author.full_name}, {i.year}, {i.genre}, {i.dds_number}, {i.isbn}\n"
     def search_book(self, name):
         for i in self.books:
             if i.name == name:
                 print(f'{i.name} bu kitob bor {i.dds_number}')
                 return i
             else:
                 print(f'{i.name} bu kitob yoq')
                 return None
author1 = Author('Ibn Xaldun', """Ibn Xaldun Abduraxman Abu Zayd Ibn Muhammad (1332-yil 27-may, Tunis – 1406-yil 17-mart, Qohira) – arab tarixchisi va faylasufi. Ibn Rushdning izdoshi. 1349–1375-yillarda Tunis, Fes, Gʻarnota, Bujjoya (Jazoirda) hukmdorlari saroyida yuqori lavozimlarda ishlagan. 1382-yil Misrga kelib, mudarrislik qilgan, umrining oxirida molikiylar mazhabi qozisi boʻlgan.
 """)
book1 = Book('Muqqadima', author1, 1389, 'siyosat', 2034, 1232323)
book2 = Book('Muqqadima2', author1, 1399, 'siyosat', 2035, 1232123)

c1 = Catalog('1-catalog')

c1.add_book(book1)
c1.add_book(book2)
c1.add_book('sariq dev')

print(c1.books)
print(c1.get_books())
c1.search_book('Muqqadima')
c1.search_book('Muqqadima3')


def main():
     while True:
         bok = 2
         choice = int(input('1.Kitobni royxati\n2.Kitob qoshinsh\n3.Kitobni qidirush\n4.Exit\n nima qilasiz: '))
         if choice == 1:
             c1.get_books()
         elif choice == 2:
             bok+=1
             print('book',bok)
             name = input('kitobni nomi: ')
             author = input('kitobni avtori: ')
             year = int(input('kitobni yili: '))
             genre = input('kitob nima haqida: ')
             dds = int(input('kitobni dds =: '))
             isbn = input('kitobni isbni =: ')
             c1.add_book(Book(name, author, year, genre, dds, isbn))
         elif choice == 3:
             name = input('kitobni nomi: ')
             if name in c1.books:
                 c1.search_book(name)
             else:
                 print('bunaqa kitob yo`q')
         else:
             print('hayir salomat bo`lin')
             break
main()
















#
#
#
#
#
#
#
#
#
#
#
#
#
# class Author:
#     def __init__(self, full_name, bio):
#         self.full_name = full_name
#         self.bio = bio
#
#
# class Book:
#     def __init__(self, name, author, year, genre, dds_number, isbn):
#         self.name = name
#         self.author = author  # Author obyekt
#         self.year = year
#         self.genre = genre
#         self.dds_number = dds_number
#         self.isbn = isbn
#
#
# class Catalog:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
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
