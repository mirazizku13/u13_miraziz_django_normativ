# list = ["salom", 13, "aolma"]
# print(list)


# name = []
# name.append("abror")
# name.append("aziz")
# print(name)



# name = []
# name.append("abror")
# name.append("aziz")
# name.pop(1)
# print(name)


# name = []
# name.append("abror")
# name.append("aziz")
# name.remove("aziz")
# name.append("ali")
# print(name)

"""
pop() → index bo‘yicha elementni qaytarib o‘chiradi
del → index bo‘yicha o‘chiradi, qiymatni qaytarmaydi
remove() → element qiymatini o‘chiradi (agar topilmasa xato beradi)
"""
# ismlar = ['Ali', 'Vali', 'Gani', 'Toshmat', 'Alisher']

# yaqinlar = []

# ali = ismlar.pop(0)
# yaqinlar.append(ali)
# toshmat = ismlar.pop(2)
# yaqinlar.append(toshmat)
# gani = ismlar.pop(1)
# yaqinlar.append(gani)
# print(yaqinlar)
# yaqinlar.sort()
# print(yaqinlar)
# print(yaqinlar + ismlar)



# num = list(range(1, 101))
# # print(num[::-1])
# num1 = []

# a = num[:10] + num[-10:] 
# print(a)
# num1.append(num[-10:])
# print(num1)




sonlar = tuple(range(1,11))
print(sonlar)
print(sonlar[3:7])


sonlar_list = list(sonlar)
sonlar_list[0] = 100  # birinchi elementni o‘zgartirish
sonlar_tuple = tuple(sonlar_list)
print("O'zgartirilgan tuple:", sonlar_tuple)