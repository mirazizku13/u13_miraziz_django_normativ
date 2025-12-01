import string
import time

# text = ('hello wold')
# temp = ''
#
# for ch in text:
#     for i in string.printable:
#         if i == ch or ch == ' ':
#             print(temp + i)
#             temp += ch
#             time.sleep(0.02)
#             break
#         else:
#             print(temp + i)
#             time.sleep(0.002)  # k

from abc import ABC, abstractmethod
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
        return f"{self.title} — {self.author.full_name} ({self.year})"


class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.issue = issue

    def locate(self):
        return f'Volume: {self.volume}, Issue: {self.issue}'

    def __str__(self):
        return f" {self.title} — Vol.{self.volume}, Issue {self.issue}"


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
        return f"💿 {self.title} — {self.artist}"


class Catalog:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.items.append(item)
            print(f"✅ '{item.title}' katalogga qo‘shildi.")
        else:
            print('Error: faqat LibraryItem obyektini qo‘shish mumkin!')

    def get_item(self):
        if not self.items:
            print(' Katalog bo‘sh!')
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

            # --- BOOK ---
            if a == '1':
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

            # --- MAGAZINE ---
            elif a == '2':
                title = input("Sarlavha: ")
                upc = input("UPC kodi: ")
                subject = input("Mavzu: ")
                volume = input("Volume: ")
                issue = input("Issue: ")
                m = Magazine(title, upc, subject, volume, issue)
                c1.add_item(m)

            # --- DVD ---
            elif a == '3':
                title = input("Sarlavha: ")
                upc = input("UPC kodi: ")
                subject = input("Mavzu: ")
                actors = input("Aktorlar (vergul bilan): ").split(',')
                director = input("Rejissor: ")
                genre = input("Janr: ")
                d = DVD(title, upc, subject, actors, director, genre)
                c1.add_item(d)

            # --- CD ---
            elif a == '4':
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
            if keyword in c1.items:
                print(f'{c1.items}')
            # results = c1.search(keyword)
            # if results:
            #     print(f"\n{len(results)} ta natija topildi:")
            #     for r in results:
            #         print(r)
            # else:
            #     print("Hech narsa topilmadi.")

        elif choice == '4':
            print('\nDasturni yakunlash.')
            print('Hayir salomat bo`ling!')
            break

        else:
            print("Noto‘g‘ri tanlov! Faqat 1,2,3,4.")


main()