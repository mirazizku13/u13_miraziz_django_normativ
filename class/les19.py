class Animal:
    def __init__(self, name, age, rangi):
        self.name = name
        self.age = age
        self.rangi = rangi
    def get_info(self):
        return f'nomi {self.name}, yoshi {self.age}, rangi{self.rangi}'
