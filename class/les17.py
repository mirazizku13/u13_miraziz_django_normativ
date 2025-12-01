# nom, narxi, soni = 'adrenaline', 200, 20

# products = {
#     'adrenaline': {'narxi': 200, 'soni': 20},
#     'coca-cola': {'narxi': 10000, 'soni': 30},
#     'morojniy': {'narxi': 20000, 'soni': 10},
#     'non': {'narxi': 5000, 'soni': 200}
# }
# for k,v in products.items():
#     products[k]["jami"] = v["soni"] * v["narxi"]
# print(products)



# summa = lambda x,y: x*y

# print(summa(2,4))



# from math import sqrt

# sonlar = list(range(1,10))

# print(sonlar)
# # empty = []
# # for i in sonlar:
# #     empty.append(i ** 2)

# # print(empty)

# kv_sonlar = list(map(lambda x:x**2, sonlar))
# print(kv_sonlar)



# from math import sqrt

# sonlar = range(11)


# matn = 'salom123'
# result_1 = list(map(lambda x:x.isalpha(), matn))
# print(result_1)



# import random as r

# sonlar = r.sample(range(100), 10)
# print(sonlar)

# juft_sonlar = list(filter(lambda x:x % 2 == 0, sonlar))
# print(juft_sonlar)
# for i in sonlar:
#     if i%2 ==0:
#         print(i,"son juft")
#     else:
#         print(i,"toq")





def factorial(number):
    if number == 1:
        return 1
    else:
        return number + factorial(number - 1)
    

print(factorial(5))

def sana(n):
    print(n)
    if n==1:
        return 1
    sana(n - 1)





def n_sonlar():
    pass