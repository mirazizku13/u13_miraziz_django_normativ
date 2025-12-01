'''
sonlar = [2, 2, 3, 2, 5, 4, 3, 2, 5, 3]

max_son = sonlar[0]
max_count = sonlar.count(max_son)
counter_common = 0

for i in sonlar[1:]:
    if sonlar.count(i) > max_count:
        max_son = i
        max_count = sonlar.count(i)
        counter_common = 0
    elif sonlar.count(i) == max_count and i != max_son:
        counter_common += 1

if counter_common >= 2:
    print("Eng ko‘p uchraydigan sonlar ko‘p")
else:
    print(max_son)
'''




# sonlar = [2, 3, 2 ,5, 4, 2, 5, 3, 3]
# # son = sonlar[0]
# # for i in sonlar:
# #     if son <i:
# #         son = i 
# # print("max son",son)
 
# total =0
# print(total)
# for i in sonlar:
#     total += i 
# print(total)



# cart = [12000, 25000, 18000, 5000]

# total = 0

# for i in cart:
#     total += i
# print(total*0.12)
# print(sum(cart)*0.12)


# prices = [100000, 50000, 20000]
# skidka = []
# for i in prices:
#     i = i * (1-0.15)
#     skidka.append(i)
# print(skidka)

words = ["py", "loop", "array", "if"]
x = []
for i in words:
    x.append(len(i))
print(x)