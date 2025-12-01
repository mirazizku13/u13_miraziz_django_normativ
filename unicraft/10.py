from abc import ABC, abstractmethod


class Computer(ABC):
    total_computers = 0
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        Computer.total_computers += 1

    @abstractmethod
    def display_info(self):
        pass


    def get_total_computers(self):
        return Computer.total_computers



class Monoblock(Computer):
    def __init__(self, brand, model, year, price, screen_size):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        print(f"Monoblock → {self.brand} {self.model} ({self.year}), {self.screen_size}\" ekran, narx: {self.price}")



class Notebook(Computer):
    def __init__(self, brand, model, year, price, battery_life):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        print(f"Notebook → {self.brand} {self.model} ({self.year}), {self.battery_life} soat batareya, narx: {self.price}")




mono = Monoblock("Apple", "iMac", 2022, 1500, 27)
note = Notebook("Lenovo", "ThinkPad", 2021, 900, 12)

mono.display_info()
note.display_info()

print(f"\nJami kompyuterlar: {Computer.total_computers}")





























