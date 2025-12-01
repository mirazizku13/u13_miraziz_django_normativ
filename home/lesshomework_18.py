class Avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = kilometr

    def get_info(self):
            return f'Madel {self.model}, \nRangi {self.rang}, \nKarobka pedach {self.korobka}, \nNarh {self.narh}'

    def update_km(self, new_km):
        self.kilometr += new_km

car1 = Avto('cobalt', 'qora', 'avtomat', '5000$', '5000')
print(car1.model)
print(car1.rang)
print(car1.korobka)
print(car1.narh)
print(car1.kilometr)

class Avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avto(self):
        return [avto.model for avto in self.avtolar]


avto1 = Avto("Cobalt", "oq", "avtomat", 15000)
avto2 = Avto("Malibu", "qora", "avtomat", 25000, 5000)

salon = Avtosalon("GM Uzbekistan", "Toshkent shahri")

salon.add_avto(avto1)
salon.add_avto(avto2)

for info in salon.get_avto():
    print(info)

avto1.update_km(1200)
print("\nYangilangan ma’lumot:")
print(avto1.get_info())