# telfon_raqamlar = {"ismi":"raqam"}


# number = int(input('nechta foydalanovchini raqamini shakilantirmoqchiz: '))


# for a in range(number):
#     ism = input("ismini kiriting: ")
#     raqam = input("raqamini kiriting: ")
    
#     telfon_raqamlar.update({ism:raqam})
# print(telfon_raqamlar)



# kitob1 ={
#     "name":"qo`rqma",
#     "type":"roman",
#     "id": 123,
#     "page": 300
# }






uz_eng = {
    "olma":"apple",
    "salom":"hi",
    "tegma":"don't touch",
}
soz = input("so'zni kiring: ")
a =uz_eng.get(soz)
if a:
    print("tarjima:",a)
else:
    print("bunday luga`t yo`q!")
