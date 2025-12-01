# sonlar = [1, 2, 3, 4, 5, 6, 7]

# def yigindi(sonlar: list) -> int:
#     total =0
#     for i in sonlar:    
#         total+=i
#     print(total)     
    
#     return 0
    
# y = yigindi(sonlar)
# print(y) # 28





# def toliq_ism_yasa(ism,familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("miraziz", "mirabdullayev")

# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")



# def summa(*args):
#     jami = 0
#     for son in args:
#         jami+=son
#     return jami


# print(summa(1,2,3))
# print(summa(4,5,6,7))



# def malumot_ber(**kwargs):
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit}: {qiymat}")

# malumot_ber(ism ="miraziz", yosh = 17, kasb = "dasturchi")


# x = 10

# def change_x():
#     global x
#     x = 20

# change_x()
# print(x)




