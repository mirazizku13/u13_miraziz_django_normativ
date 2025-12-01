from oop_less22 import Catalog,Magazine,Book

def main():
    catalog = Catalog("1-catalog")
    while True:
        choice = input('1. royxatlar\n2.kitob qoshish\n3.kitob qidirish\n4.Exit')
        if choice == '1':
            catalog.get_items()
        elif choice == '2':
            choice = input('nima qoshmoqchisiz kutubxonaga.(book,cd,magazine,dvd)')
            if choice not in ['book','cd',"magazine","dvd"]:
                print('Siz mavzudan chiqib ketdingiz')
                continue
            title = input("Sarlavha: ")
            upc = input("UPC kodi: ")
            subject = input("Mavzu: ")
            if choice.lower()=='book' or choice.lower()=='1':
                isbn = input("ISBN: ")
                dds = input("DDS raqami: ")
                item = Book(title, upc, subject, isbn, 'Gafur gulom',dds)
            elif choice.lower() == 'magazine' or '3':
                volume = input("volume: ")
                issue = input("issue: ")
                item = Magazine(title, upc, subject,volume,issue)
            else:
                print('Siz mavzudan chiqib ketdingiz')
                continue
            catalog.add_items(item)

        elif choice == "3":
            q = input('title ni kiriting>>>>')
            for i in catalog.search(q):
                print(i.get_info())

        elif choice == "4":
            print("Dastur yakunlandi.")
            break

        else:
            print("Noto‘g‘ri tanlangan dastur")

if __name__ == '__main__':
    main()