# import pickle
#
# a = {
#     "Ali":12,
#     "Vali":22,
#     "gani":22,
#     "Salim":32
# }
#
# with open('abaut.dat', 'wb') as f:
#     pickle.dump(a, f)
# with open('abaut.dat', 'rb') as f:
#     talaba = pickle.load(f)
# print(talaba)
import pickle

#
# def write_data(data):
#     with open('library.dat', 'wb') as f:
#         pickle.dump(data, f)
#
# def read_data(data):
#     with open('library.dat', 'rb') as f:

# import pickle
#
# talaba = {"Ismi":"ALi", "Familiyasi":"Azimov", "Yili":"2002", "Kursi":1}
#
# class Talaba():
#     def __init__(self, nome, age, kurse):
#         self.nome = nome
#         self.age = age
#         self.kurse = kurse
#
#     def get_info(self):
#         return f"Ismi: {self.nome} \nYili: {self.age} \nKursi: {self.kurse}"
#
#
# t1 = Talaba("aziz", 20, 2)
# with open("talaba.pkl", "wb") as f:
#     pickle.dump(t1, f)
# with open("talaba.pkl", "rb") as f:
#     t2 = pickle.load(f)
# print(t1.get_info())



import json

with open("talaba.json", 'r') as f:
    data = json.load(f)

data['dorilar'][0]['nomi'] = "parastamol"
data['dorilar'][0]['miqdori'] = 1,5

data['dorilar'][1]['nomi'] = "stramon"
data['dorilar'][1]['miqdori'] = 1,5

with open('talaba.json', 'w') as f:\
    json.dump(data, f)
print(data)