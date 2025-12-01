# # 1
# batery = int(input("telifon zaryadini kiriting: "))
# charg = bool(int(input("telifon zaryadkadami: (1-ha 0-yo`q)")))
# a = bool(batery <=20)
# b =charg or not a 
# print(b)

# 2
# monny = int(input("naqt pulingizni kiriting: "))
# tiket = bool(int(input("chipta sotib olinganmi: (1-ha 0-yo`q)")))
# a = bool(monny <=50000)
# b =tiket and not a 
# print(b)

# 3
# pin = '12345'
# clinent = input("prloni kiring: ")
# print(pin == clinent)

# 4
# work = int(input("ishtirok qilgani kiriting: '%` da'"))
# pay = bool(int(input("to‘lov to‘langanmi: (1-ha 0-yo`q)")))
# a = bool(work <=80)
# b =pay or not a 
# print(b)

# 5
# age = int(input("yoshingizni kiriting: "))
# work = bool(int(input("ish joyiz bormi: ")))
# oylik = int(input("oylik 5 milliondan kam bo‘lmasligi kerak:"))
# royhat = bool(int(input("qora royhatdamisiz: 0-yoq 1-ha")))
# a = bool(age <=22)
# o = bool(oylik <=5000000)
# total = a and work and o and not royhat
# print(total)

# 6
# age = int(input("yoshingizni kiriting: "))
# tibiy = bool(int(input("tibbiy ko`rikdan o`tganmi: 0-yoq 1-ha")))
# test = int(input("jismoniy test natijasi: "))
# doping = bool(int(input("doping aniqlanmaganmi: ")))
# a = bool (age >= 18)
# t = bool (test >= 70)
# total = a and tibiy and t and not doping
# print(total)

# 7
# punkt = bool(int(input("mahsulot omborda mavjudmi: 0-yoq 1-ha: ")))
# pay = bool(int(input("foydalanuvchi to‘lov qilganmi: 0-yoq 1-ha: ")))
# manzil = bool(int(input("foydalanuvchi manzil kiritganmi: ")))
# total = punkt and pay and manzil
# print(total)

# 8
# txt = input("gmailni kiriting: ")
# print(".com" and "@"in txt)

# 9
# tekst = input("Foydalanuvchi nomi: ")
# a = tekst.isalpha()
# uzunligi = bool(len(tekst) <= 3)
# b = tekst.islower()
# total = a and uzunligi and b
# print(total)

# 10
# tel_raqam = input("telifon raqamni kirkiting: ")
# tel =tel_raqam.isdigit()
# uzunligi = bool(9 <= len(tel_raqam)  <= 12 )
# a = ("+998" in tel_raqam or len(tel_raqam) ==9)
# total = tel and uzunligi and a
# print(total)

# 11
# fayel = input("fayel nomi: ")
# a = (".pdf" in fayel)
# b = ("*" in fayel) or ("/" in fayel) or ("\\" in fayel) or (" " in fayel)
# toatl = a and not b
# print(toatl)


