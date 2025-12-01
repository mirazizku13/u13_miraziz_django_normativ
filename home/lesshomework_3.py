# #№1
# print("O`zbekiston Vatanim mani!!!")
# #№2
tezlik= int(input("tezlikni kiriting: "))
masofa= int(input("masofani kiriting: "))
total = masofa/tezlik
print(total,"vaqda bosib otgan")
# #№3
# '''
# 18.09.2025
# miraziz
# yosh 17
# toshkent
# '''
# # №4
# print("Notes from Day 1")
# print("The print statement is used to output strings")
# print("Strings are strings of characters")
# print("String Concatenation is done with the + sign")
# print("New lines can be created with a \ and the letter n")
# # №5
# a = int(input("1-son: "))
# b = int(input("2-son: "))
# print(a,b)
# a,b = b,a
# print(a,b)
# # №6
# kocha = "Bogbon kochasi,"
# mahalla = "Soglom mahallasi,"
# tuman = "Bodomzor tumani,"
# viloyat = "Samarqand viloyati."
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil)

# print(kocha.title())         # Har bir so‘zning bosh harfini katta qiladi
# print(mahalla.upper())       # Barcha harflarni katta qiladi
# print(tuman.lower())         # Barcha harflarni kichik qiladi
# print(viloyat.capitalize())  # Faqat birinchi so‘zni katta qiladi
# # №7
# a = int(input("1-soni kiriting: "))
# b = int(input("2-soni kiriting: "))
# yigindi = a + b
# ayirma = a - b
# kopaytma = a * b
# bolish = a / b
# qoldiqli = a // b
# print(a,"+",b,"=",yigindi)
# print(a,"-",b,"=",ayirma)
# print(a,"*",b,"=",kopaytma)
# print(a,"/",b,"=",bolish)
# print(a,"//",b,"=",qoldiqli)



















# # №1
# a = int(input("1-soni kiriting: "))
# b = int(input("2-soni kiriting: "))
# yigindi = a + b
# ayirma = a - b
# kopaytma = a * b
# bolish = a / b
# qoldiqli = a // b
# print(a,"+",b,"=",yigindi)
# print(a,"-",b,"=",ayirma)
# print(a,"*",b,"=",kopaytma)
# print(a,"/",b,"=",bolish)
# print(a,"//",b,"=",qoldiqli)
# # №2
# tuhilgan = int(input("tug`ilgansana:"))
# yill= 2025
# c = yill - tuhilgan
# print("mening yoshim: ",c)
# # №3

# a1 = int(input("1-baho: "))
# a2 = int(input("2-baho: "))
# a3 = int(input("3-baho: "))

# c = (a1 + a2 + a3)/3
# print(c)

#№4
 
# ism = "Ali" 
# yosh = 20 
# print("Salom, "+ism+"Sizning yoshingiz: ",yosh) 


# №5
# a = int(input("tomin: "))
# print("tomon",a*2)
# print("primetr",a*4)
# №6
# r= int(input("radius: "))
# l = 2*3.14*r
# s = 3.14*r**2
# print(l,s)
# # №7
# son = int(input("3 xonali sonni kiriting: "))
# a = str(son)
# birlik= int(a[2])
# onlar = int(a[1])
# yuzlar = int(a[0])
# print(birlik+onlar+yuzlar)

# bir = son%10
# onlik = son//10%10
# yuzlik = son//100
# print(bir+onlik+yuzlik)
#№8
# a = int(input("Uchish vaqtini kiriting : "))
# b = int(input("Yetib Borish vaqti : "))
# print(b - a , "Daqiqada yetib borasiz")
# uchish_soati = int(input("Uchish soatini kiring: "))
# uchish_minut = int(input("uchish minutini kiring: "))

# parvoz_davomiyligi = int(input('qancha vaqt uchdi: '))

# yetib_borish_soati = uchish_soati + (parvoz_davomiyligi + uchish_minut) //60
# yetib_borish_minuti = (parvoz_davomiyligi + uchish_minut) % 60

# print(f'yetib borish vaqti: {yetib_borish_soati}:{yetib_borish_minuti}')
# #№9
# dollar= 12300
# a = int(input("Qancha? "))
# som = dollar * a
# print("Natija:",a,"dollar =",som,"sum")

#№10
# c = int(input("haroratni slesida kirting: "))
# f = c*9/5 + 32
# print(c)
# print(f)
# print("Natija:",c,"Selsiya =",f,"Farengeyt")

#№11
# son = int(input("2 xonali son kiring: "))
# bir = son%10
# onlik = son//10%10
# print("Son:",son)
# print("O`nlik:",onlik)
# print("Birlik:",bir)

# #12
# gaplashdi= int(input("foyalangan daqiyqa: "))
# narxi = 500
# jami = gaplashdi * narxi
# print("jami:",jami)


# #13
# odamlar_soni = 47
# orindiqlar = 15
# nechta_avtobus = odamlar_soni / orindiqlar
# print(nechta_avtobus)


# #14
# Olma = 5000
# Banan = 7000
# Nok = 6000
# print(2*(Olma + Banan + Nok))