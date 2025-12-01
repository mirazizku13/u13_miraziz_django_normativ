# 1

# a = input("ismingizni  kiring:  ")
# b = int(input("yoshingiz:  "))
# c = 2025 - b
# print(f"sizning ismingiz {a}, yoshingiz {b}, tugi`lgan yiliz {c}")

# def malumot_ber(**kwargs):
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit}: {qiymat}")

# malumot_ber(ism ="miraziz", yosh = 17, yill = 2008)



# 2
# def son(a):
#     b = a*a
#     c = a*a*a
#     print(f"siz kritgan son {a}, \nkvadrati {b}, \nkubi {c}")
# a = int(input("son kiriting: "))
# son(a)


# 3
# def son(a):
#     if a%2 ==0:
#         print(f"{a} juft son")        
#     else:
#         print(f"{a} toq son")

# a = int(input("sonni kiriting: "))
# son(a)


# 4
# def son(a, b):
#     if a>b:
#         print(f"{a} kota {b} dan")
#     elif b>a:
#         print(f"{b} kota {a} dan")
#     elif a == b:
#         print(f"a={a} va b={b} teng")
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# son(a,b)


# 5
# def daraja(x, y):
#     print(f"{x} ning {y}-darajasi = {x ** y}")

# x = int(input("x sonini kiriting: "))
# y = int(input("y sonini kiriting: "))

# daraja(x, y)


# 6

# def bolinish_alomatlari(n):
#     """
#     n sonini 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiradi.
#     Faqat qoldiqsiz bo'linadiganlar konsolga chiqariladi.
#     """
#     for i in range(2, 11):
#         if n % i == 0:
#             print(f"{n} {i} ga qoldiqsiz bo'linadi")
#         else:
#             print(f"{n} {i} ga qoldiqli bo'linadi")
        
# bolinish_alomatlari(71)



# 7
# def malumot_ber(**kwargs):
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit}: {qiymat}")
# ism1 = input("ismingiz: ")
# yosh1 = int(input("yoshingiz: "))
# yill1 = 2025-yosh1
# joy = input("tugilgan joy: ")
# email1 = input("pochtangiz: ")
# tel = input("telifon ragam: ")

# malumot_ber(ism =ism1, yosh = yosh1, yill = yill1, t_joy= joy, email= email1, tell = tel)


# 8

# def malumot_ber(**kwargs):
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit}: {qiymat}")
#     print("-" * 30)  


# a = int(input("Nechta mijoz kiritasiz: "))

# i = 1
# while i <= a:
#     print(f"\n{i}-mijoz ma'lumotlari:")
#     ism1 = input("Ismingiz: ")
#     yosh1 = int(input("Yoshingiz: "))
#     yill1 = 2025 - yosh1
#     joy = input("Tug‘ilgan joy: ")
#     email1 = input("Email: ")
#     tel = input("Telefon raqam: ")

    
#     malumot_ber(ism=ism1, yosh=yosh1, yill=yill1, t_joy=joy, email=email1, tell=tel)

#     i += 1

# 9
# def son(a,b,c):
#     if a >= b and a >= c:
#         print(f"a = {a} eng katta son")
#     elif b >= a and b >= c:
#         print(f"b = {b} eng katta son")
#     else:
#         print(f"c = {c} eng katta son")

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# son(a,b,c)

# a = int(input("aylananing radiusini kiriting: "))

# def aylana_malumoti(r):
#     d = a *2
#     p = r*3.14
#     y = (r*3.14) * 2
#     aylana = {
#         "diametri":d,
#         "perimetri":p,
#         "yuzi":y
#     }
#     return aylana

# print(aylana_malumoti(a))