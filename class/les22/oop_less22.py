from abc import ABC, abstractmethod


class Libraryltem(ABC):
    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject

    @abstractmethod
    def get_locate(self):
        pass

    def get_info(self):
        return f'{self.title}: {self.upc} {self.subject}'


class Book(Libraryltem):
    def __init__(self, title, upc, subject, isbn, authors, dds_number):
        super().__init__(title, upc, subject)
        self.isbn = isbn
        self.authors = authors
        self.dds_number = dds_number

    def get_locate(self):
        return self.dds_number


class Magazine(Libraryltem):
    def __init__(self, title, upc, subject, volume, issue):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.issue = issue

    def get_locate(self):
        return self.volume


class DVD(Libraryltem):
    def __init__(self, title, upc, subject, actors, director, genre):
        super().__init__(title, upc, subject)
        self.actors = actors
        self.director = director
        self.genre = genre

    def get_locate(self):
        return self.genre


class Cd(Libraryltem):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)
        self.artist = artist

    def get_locate(self):
        return self.artist


class Author:
    def __init__(self, name):
        self.name = name


class Catalog:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def search(self, title):
        s = []
        for item in self.items:
            if title.lower() == item.title.lower():
                s.append(item)
        return s

    def get_items(self):
        for i in self.items:
            print(f'{i.get_info()}')

