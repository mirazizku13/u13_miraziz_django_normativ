import random

# comp_number = random.randint(1,10)
# son = int(input("kompitur son oyladi siz taxmin qilib koring"))
# guess = 1

# while comp_number!= son:
#     if comp_number>son:
#         son = int(input("kattaroq son taxmin qilib ko`ring"))
#     else:
#         son = int(input("kichkinaroq son taxmin qilib ko`ring"))
#     guess+=1

# print(f"Togri son topdingiz, {guess} ta urinish")


# son = int(input("random son kiring: "))

# pc = random.randint(1,10)
# guess = 1

# while son != pc:
#     if son>pc:
#         pc = random.randint(1,10)
#         print("kattaroq son",pc)
#         guess +=1
#     elif son<pc:
#         pc = random.randint(1,10)
#         print("kichkinaroq son")
#         guess +=1
#     else: 
#         print("topdi",pc, guess)
#         break




# import random

# son = int(input("1 dan 10 gacha bo'lgan son o'ylang: "))

# guess = 0
# while True:
#     pc = random.randint(1, 10)
#     guess += 1

#     if pc > son:
#         print(f"Kompyuter {pc} dedi — sizning son kichikroq.")
#     elif pc < son:
#         print(f"Kompyuter {pc} dedi — sizning son kattaroq.")
#     else:
#         print(f"Kompyuter topdi! 🎯 Son: {pc}, urinishlar soni: {guess}")
#         break





phone = {
    'Ali':"+998901233456"
}


while True:
   
    ism  = input('ism kiriting>>>')
    raqam = input('tel raqam kiritng>>>')
    answer = input("davom etamizmi? (ha, yo`q)")
    
    phone[ism] =raqam
    if answer.lower() == 'yoq':
        break
print(phone)