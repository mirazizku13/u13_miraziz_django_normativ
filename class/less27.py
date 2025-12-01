# import csv
#
# # with open('talaba.csv') as f:
# #     reader = csv.reader(f)
# #     total = 0
# #     for index, i in enumerate(reader):
# #         if index == 0:
# #             continue
# #         total += int(i[1])
# #     print(total / index)
#
# # with open('talaba.csv') as f:
# #     reader = csv.DictReader(f)
# #     ages = []
# #     for i in reader:
# #         ages.append(int(i.get("age")))
# #     print(sum(ages)/len(ages))
#
# # logging yozish
#
# import logging
# import pickle
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='app.log',
#     filemode='a',
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
#
# # logging.debug('debug ishladi')
#
#
# def write_data(data):
#     with open('library.dat', 'wb') as f:
#         pickle.dump(data, f)
#
#
# def read_data():
#     try:
#         with open('library.dat', 'rb') as f:
#             data = pickle.load(f)
#         return data
#     except:
#         return None
#
#
# from abc import abstractmethod, ABC
#
#
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
#
# class Author:
#     def __init__(self, full_name, bio):
#         self.full_name = full_name
#         self.bio = bio
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
#         return f'DDS raqami: {self.dds_number}'
#
#     def __str__(self):
#         return f"📘 {self.title} — {self.author.full_name} ({self.year})"
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
#     def __str__(self):
#         return f"📰 {self.title} — Vol.{self.volume}, Issue {self.issue}"
#
#
# class DVD(LibraryItem):
#     def __init__(self, title, upc, subject, actors, director, genre):
#         super().__init__(title, upc, subject)
#         self.actors = actors
#         self.director = director
#         self.genre = genre
#         logging.info('DVD clasiga item qo')
#     def locate(self):
#         return f"Aktorlar: {', '.join(self.actors)}"
#
#     def __str__(self):
#         return f"🎬 {self.title} — Rejissor: {self.director}"
#
#
# class CD(LibraryItem):
#     def __init__(self, title, upc, subject, artist):
#         super().__init__(title, upc, subject)
#         self.artist = artist
#
#     def locate(self):
#         return f"Ijrochi: {self.artist}"
#
#     def __str__(self):
#         return f"{self.title} — {self.artist}"
#
#
# class Catalog:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add_item(self, item):
#         if isinstance(item, LibraryItem):
#             self.items.append(item)
#             logging.debug(f"{item.title} katalogga qo‘shildi.")
#             write_data(self)
#         else:
#             print('Error: faqat LibraryItem obyektini qo‘shish mumkin!')
#
#     def get_item(self):
#         if not self.items:
#             print('📭 Katalog bo‘sh!')
#         else:
#             for item in self.items:
#                 print(item)
#
#     def search(self, keyword):
#         result = []
#         for item in self.items:
#             if keyword.lower() in item.title.lower() or keyword.lower() in item.subject.lower():
#                 result.append(item)
#         return result
#
#
# def main():
#     data = read_data()
#     if data:
#         c1 = data
#     else:
#         c1 = Catalog('1-katalog')
#         write_data(c1)
#     while True:
#         print('\n==================================')
#         print("========   KATALOG MENU   ========")
#         print('==================================')
#         print("1. Itemlar ro‘yxati")
#         print("2. Yangi item qo‘shish")
#         print("3. Itemni qidirish")
#         print("4. Chiqish")
#
#         choice = input("Tanlov: ")
#
#         if choice == '1':
#             print('\nKatalogdagi barcha itemlar:')
#             c1.get_item()
#
#         elif choice == '2':
#             print('\nQanday item qo‘shmoqchisiz?')
#             print('1. Book\n2. Magazine\n3. DVD\n4. CD')
#             a = input("Tanlang (1-4): ")
#
#             if a == '1' or a.lower() == 'book':
#                 title = input("Sarlavha: ")
#                 upc = input("UPC kodi: ")
#                 subject = input("Mavzu: ")
#                 author_name = input("Muallif ismi: ")
#                 author_bio = input("Muallif haqida: ")
#                 author = Author(author_name, author_bio)
#                 year = input("Yil: ")
#                 genre = input("Janr: ")
#                 dds = input("DDS raqami: ")
#                 isbn = input("ISBN: ")
#                 b = Book(title, upc, subject, author, year, genre, dds, isbn)
#                 c1.add_item(b)
#             elif a == '2' or a.lower() == 'magazine':
#                 title = input("Sarlavha: ")
#                 upc = input("UPC kodi: ")
#                 subject = input("Mavzu: ")
#                 volume = input("Volume: ")
#                 issue = input("Issue: ")
#                 m = Magazine(title, upc, subject, volume, issue)
#                 c1.add_item(m)
#
#
#             elif a == '3' or a.lower() == 'dvd':
#                 title = input("Sarlavha: ")
#                 upc = input("UPC kodi: ")
#                 subject = input("Mavzu: ")
#                 actors = input("Aktorlar (vergul bilan): ").split(',')
#                 director = input("Rejissor: ")
#                 genre = input("Janr: ")
#                 d = DVD(title, upc, subject, actors, director, genre)
#                 c1.add_item(d)
#
#
#             elif a == '4' or a.lower() == 'cd':
#                 title = input("Sarlavha: ")
#                 upc = input("UPC kodi: ")
#                 subject = input("Mavzu: ")
#                 artist = input("Ijrochi: ")
#                 cd = CD(title, upc, subject, artist)
#                 c1.add_item(cd)
#
#             else:
#                 print("Noto‘g‘ri tanlov!")
#
#         elif choice == '3':
#
#             keyword = input("\nQidirilayotgan so‘zni kiriting: ")
#             results = c1.search(keyword)
#             if results:
#                 print(f"\n{len(results)} ta natija topildi:")
#                 for r in results:
#                     print(r)
#             else:
#                 print("Hech narsa topilmadi.")
#
#         elif choice == '4' or choice == '':
#             print('\nDasturni yakunlash.')
#             print('Hayir salomat bo`ling!')
#             break
#
#         else:
#             print("Noto‘g‘ri tanlov! Faqat 1,2,3,4.")
#
# if __name__ == '__main__':
#     main()






import csv

# with open('talaba.csv') as f:
#     reader = csv.reader(f)
#     total = 0
#     for index, i in enumerate(reader):
#         if index == 0:
#             continue
#         total += int(i[1])
#     print(total / index)

# with open('talaba.csv') as f:
#     reader = csv.DictReader(f)
#     ages = []
#     for i in reader:
#         ages.append(int(i.get("age")))
#     print(sum(ages)/len(ages))

# logging yozish

import logging
import pickle

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# logging.debug('debug ishladi')


def write_data(data):
    with open('library.dat', 'wb') as f:
        pickle.dump(data, f)


def read_data():
    try:
        with open('library.dat', 'rb') as f:
            data = pickle.load(f)
        return data
    except Exception as e:
        logging.error(f'error: {e}')
        return None


from abc import abstractmethod, ABC


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
        logging.info('DVD classidan obyekt olindi')

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
            logging.debug(f"{item.title} katalogga qo‘shildi.")
            write_data(self)
        else:
            print('Error: faqat LibraryItem obyektini qo‘shish mumkin!')
            logging.warning('warning: faqat LibraryItem obyektini qo‘shish mumkin!')

    def get_item(self):
        if not self.items:
            print('📭 Katalog bo‘sh!')
            logging.info('INFO: Katalog bo`sh!')
        else:
            for item in self.items:
                print(item)

    def search(self, keyword):
        result = []
        for item in self.items:
            if keyword.lower() in item.title.lower() or keyword.lower() in item.subject.lower():
                result.append(item)
        return result


def main():
    data = read_data()
    if data:
        c1 = data
    else:
        c1 = Catalog('1-katalog')
        write_data(c1)
    while True:
        print('\n==================================')
        print("========   KATALOG MENU   ========")
        print('==================================')
        print("1. Itemlar ro‘yxati")
        print("2. Yangi item qo‘shish")
        print("3. Itemni qidirish")
        print("4. Chiqish")

        choice = input("Tanlov: ")

        if not choice.isdigit():
            logging.critical('critical: raqam tanlanishi kerak')
            raise ValueError('raqam tanlsh kerak ')

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
                print("Noto‘g‘ri tanlov! (1 dan 4gacha yoki nimini yozing!)")
                logging.info('Noto‘g‘ri tanlov! (1 dan 4gacha yoki nimini yozing!)')

        elif choice == '3':
            keyword = input("\nQidirilayotgan so‘zni kiriting: ")
            results = c1.search(keyword)
            if results:
                print(f"\n{len(results)} ta natija topildi:")
                for r in results:
                    print(r)
            else:
                print("Hech narsa topilmadi.")
                logging.debug('DEBUG: Hechnarsa topilmadi')

        elif choice == '4' or choice == '':
            print('\nDasturni yakunlash.')
            print('Hayir salomat bo`ling!')
            logging.info("INFO: Dastur yakunlandi")
            break

        else:
            print("Noto‘g‘ri tanlov! Faqat 1,2,3,4.")
            logging.critical(f'critical: 1 dan 4 gacha raqam tanlanishi kerak{choice}')


if __name__ == '__main__':
    main()

    # user = int(input("user ismini kiring:"))
    # user_pass = input('user paroli:')

    # c1 = Catalog('salom')
    # c1.add_item('dsadsa')
