# 1---------------------------------------------------------------------------------------------
# balance = 1000

# while balance > 0:
#     try:
#         amount = int(input(f"Balansingiz: ${balance}. Qancha yechmoqchisiz? "))
#     except ValueError as e:
#         print(f"Xatolik {e}")
#     else:
#         if amount > balance:
#             print("Sizda yetarli mablag‘ yo‘q!")
#             continue

#         balance -= amount
        
#         work = input("Yana yechasizmi? (ha, yoq): ").islower()
#         if work not in ["ha",  "yoq"]:
#             print("Faqat 'ha' yoki 'yoq' deb yozing!")
#         else:
#             if work.lower() == "yoq":
#                 print(f"Sizning hisobingizda ${balance} qoldi.")
#                 break
#             else:
#                 print(f"Hozirgi balans: ${balance}")

#             if balance <= 0:
#                 print("Pul qolmadi!")
#                 break
# ------------------------------------------------------------------------------------------------------------------------------------
# 2-------------------------------------------------------------------------------------------------------------------------------------------
# total = 0

# while True:
#     item = input("Mahsulot narxini kiriting yoki 'stop' deb yozing: ").lower()
#     if item == "stop":
#         print(f"Barcha mahsulotlarning umumiy narxi: {total} so‘m")
#         break
#     try:
#         price = int(item)
#         if price < 0:
#             print("Narx manfiy bo‘lishi mumkin emas!")
#             continue
#         total += price
#     except ValueError:
#         print("Iltimos, faqat raqam kiriting yoki 'stop' deb yozing!")

# --------------------------------------------------------------------------------------------------------------------------------------------
# 3--------------------------------------------------------------------------------------------------------------------------------------------
# goal = 10000
# kun = 0

# while goal >= 0:
#     try:
#         qadam = int(input(f'{kun+1} - kun yurgan qadamingizni kiriting>>>'))
#     except ValueError as e:
#         print(f"xatolik{e}")
#     else:
#         goal -= qadam
#         kun+=1

# print(f'siz 10000 qadamlik maqsadingizni {kun} kunda bajardingiz')
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 4--------------------------------------------------------------------------------------------------------------------------------------------
# month = 1
# paid_months = 0
# while month <= 12:
#     status = input(f"{month}-oy ijarani to‘ladingizmi? (ha/yo‘q): ")
#     if status not in ["ha", "yoq"]:
#         print("Faqat 'ha' yoki 'yoq' deb yozing!")
#     else:
#         month +=1
#         if status == "ha":
#             paid_months +=1
#         elif status == "yoq":
#             print("tolab qoyin")    
#         if paid_months == 12:
#             print(f"Siz {paid_months} oy ijarani to‘ladingiz.")
#             break
#         elif month == 12:
#             print(f"{month} - oy Siz {paid_months} oy ijarani to‘ladingiz.")
#             break
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 5--------------------------------------------------------------------------------------------------------------------------------------------------------
# kelajak_pul = 5000000

# while True:
#     try:
#         a = int(input("qancha pul qo`shmoqchisiz: "))
#     except ValueError as e:
#         print(f"Xatolik {e}")
#     else:
#         kelajak_pul -=a
#         print(kelajak_pul)
#         if kelajak_pul <=0:
#             print(f"tabriklayman siz 5 milon pul yeg`dingiz")
#             break
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# vazifa = []
# while True:
    
#     ish_jadvali = input("Har bir ishni kiriting yoki 'exit ' deb yozing ... ")

#     if ish_jadvali.lower() =='exit':
#         break
#     elif not ish_jadvali:
#         print("Bo‘sh yozuv kiritmang!")
#         continue
#     else:
#         vazifa.append(ish_jadvali)

# for i in vazifa:
#     print(f"Vazifalar --- {i}")