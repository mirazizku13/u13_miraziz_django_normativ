class Avto:
    avto_number = 0
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        Avto.avto_number += 1

    def get_info(self):
        return f'{self.name} {self.model} {self.year}'

avto1 = Avto('nexia3', 'chevrolet', '2023')
avto2 = Avto('nexia3', 'chevrolet', '2023')
avto3 = Avto('nexia3', 'chevrolet', '2023')
print(avto1.name)
print(avto1.get_info())
print(Avto.avto_number)