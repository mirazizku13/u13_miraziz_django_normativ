# # a = int(input("1-sonni kiriting: "))
# # b = int(input("2-sonni kiriting: "))
# # c = input("amalni kiriting: (+,-,*,/)")
# # if c == "+":
# #     print(a,"+",b,"=",a+b)
# # elif c == "-":
# #     print(a,"-",b,"=",(a-b))
# # elif c == "*":
# #     print(a,"*",b,"=",(a*b))
# # elif c == "/":
# #     print(a,"/",b,"=",(a//b))
# # else:
# #     print("amal hato ")



# # a = int(input("tug`ilgan yilizni kirint: "))
# # b = 2025-a
# # print("sizning yozingiz",b)

#     # a1 = int(input("1-kinining reytingi: "))
#     # a2 = int(input("2-kinining reytingi: "))
#     # a3 = int(input("3-kinining reytingi: "))

#     # c = (a1+a2+a3)/3
#     # print(c)


# # ism = "Ali"
# # yosh = 20
# # print(f"Salom, " , ism , "Sizning yoshingiz: " , yosh)



# # a = int(input("Kvadratning tomonini kiriting: "))

# # yuza = a * a
# # perimetr = 4 * a

# # print("Yuza:", yuza)
# # print("Perimetr:", perimetr)



# # r= int(input("radius: "))
# # l = 2*3.14*r
# # s = 3.14*r**2
# # print(l,s)


# #7
# # 3 xonali son
# son = 123
# yuzlik = son // 100
# onlik = (son // 10) % 10
# birlik = son % 10
# yigindi = yuzlik + onlik + birlik
# print(f"{yuzlik} + {onlik} + {birlik} = {yigindi}")
# #8
# uchish_soati = 13
# uchish_daqiqasi = 45
# parvoz_davomiyligi = 125
# jami_daqiqalar = uchish_soati * 60 + uchish_daqiqasi + parvoz_davomiyligi
# qo_nish_soati = (jami_daqiqalar // 60) % 24
# qo_nish_daqiqasi = jami_daqiqalar % 60
# print(f"Yetib borish vaqti: {qo_nish_soati:02}:{qo_nish_daqiqasi:02}")
# #9
# kurs=12.300
# dollar=100
# sum=dollar*kurs
# print(f"{dollar}dollar=sum{sum}")
# #10 # Foydalanuvchidan Selsiy haroratini so'rash
# celsius = float(input("Selsiyda haroratni kiriting:"))
# fahrenheit = celsius*9/5 + 32
# print(f"Natija: {fahrenheit}°F")
# #11
# son = int(input("2 xonali son kiriting: "))
# onlik = son // 10
# birlik = son % 10
# print(f"O'nlik raqami: {onlik}")
# print(f"Birlik raqami: {birlik}")
# #12
# daqiqa_narxi = 500
# daqiqalar = 7
# umumiy_narx = daqiqalar * daqiqa_narxi
# print(f"Umumiy narx: {umumiy_narx} so'm")
# #13
# odamlar_soni = 47
# orindiqlar_soni = 15
# avtobuslar_soni = (odamlar_soni + orindiqlar_soni - 1)//orindiqlar_soni
# print(f"Kerakli avtobuslar soni: {avtobuslar_soni}")
# #14
# olma_narxi = int(input("Olma narxini kiriting (so'm): "))
# banan_narxi = int(input("Banan narxini kiriting (so'm): "))
# nok_narxi = int(input("Nok narxini kiriting (so'm): "))
# miqdor = 2
# umumiy_narx = miqdor * (olma_narxi + banan_narxi + nok_narxi)
# print(f"Umumiy to'lov: {umumiy_narx} so'm")


# a = int(input("sonni kiriting: "))
# if a <0:
#     b =a + 1
#     print(b)
# else:
#     print(a)

# if a >0:
#     b = a +1
#     print(b)
# else:
#     print(a)

# a = int(input("sonni kiriting: "))
# if a <0:
#     b = a +1
#     print(b)
# else:
#     b = a-2
#     print(b)

# a = int(input("sonni kiriting: "))
# if a >0:
#     b = a+1
#     print(b)
# elif a == 0:
#     a = 10
#     print(a)
# elif a <0:
#     b = a-2
#     print(b)


# a1 = int(input("1-sonni kiring: "))
# a2 = int(input("2-sonni kiring: "))
# a3 = int(input("3-sonni kiring: "))

# count = 0

# if a1 > 0:
#     count += 1
# if a2 > 0:
#     count += 1
# if a3 > 0:
#     count += 1

# print("Musbat sonlar soni:", count)

# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))

# count = 0
# count2 = 0
# if a > 0:
#     count += 1
# if b > 0:
#     count += 1
# if c > 0:
#     count += 1

# if a < 0:
#     count2 += 1
# if b < 0:
#     count2 += 1
# if c < 0:
#     count2 += 1

# print("Musbat sonlar soni:", count)
# print("Manfiy sonlar soni:", count2)

















































                    











# print("Pythondagi primitive, str int float bool")
# print("none == qiymat yoki bo'shliqning etishmasligi")
# print("== bu tenglik operatori \n is bu identifikatsiya operatori")


# age = 17
# if age > 18:
#     label = "Adult"
# else:
#     label = "Minor"

# age = 17
# if age > 18:
#     label = "Adult"
# else:
#     label = "Minor"
# print(label)

# nums = [1,2,3,4,5,6]
# evens = []
# for num in nums:
#     if nums % 2 == 0:
#          evens.append(num)
# print(evens)

# fruits = ["apple", "banana", "pear"] 
# for item in fruits: 
#     print(item)
