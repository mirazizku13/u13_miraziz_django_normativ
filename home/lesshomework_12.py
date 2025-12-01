# balance = 1000

# while balance > 0:
#     amount = int(input(f"Balansingiz: ${balance}. Qancha yechmoqchisiz? "))

#     if amount > balance:
#         print("Sizda yetarli mablag‘ yo‘q!")
#         continue

#     balance -= amount

#     work = input("Yana yechasizmi? (ha, yoq): ")

#     if work.lower() == "yoq":
#         print(f"Sizning hisobingizda ${balance} qoldi.")
#         break
#     else:
#         print(f"Hozirgi balans: ${balance}")

#     if balance <= 0:
#         print("Pul qolmadi!")
#         break







# total = 0
# while True:
#     item = input("Mahsulot narxini kiriting yoki 'stop' deb yozing: ")
#     if item == "stop":
#         print(f"umumuy summa {total}")
#         break
#     total +=item
#     print(total)












# qadam = 0
# day = 1
# while True:
#     a = int(input(f"{day} - kun. qancha qadam bosdingiz: "))
#     qadam +=a
#     day +=1
#     if qadam >=10000:
#         print(f"{day} - sunda {qadam} bosdingiz")
#         break
#     else:
#         print(f"{day}- kun ichada {qadam}- qadam")









# month = 1
# paid_months = 0
# while month <= 12:
#     status = input(f"{month}-oy ijarani to‘ladingizmi? (ha/yo‘q): ")
#     month +=1
#     if status == "ha":
#         paid_months +=1
    
#     if paid_months == 12:
#         print(f"Siz {paid_months} oy ijarani to‘ladingiz.")
#         break
#     elif month == 12:
#         print(f"{month} - oy Siz {paid_months} oy ijarani to‘ladingiz.")
#         break






# kelajak_pul = 5000000

# while True:
#     a = int(input("qancha pul qo`shmoqchisiz: "))
#     kelajak_pul -=a
#     print(kelajak_pul)
#     if kelajak_pul <=0:
#         print(f"tabriklayman siz 5 milon pul yeg`dingiz")
#         break




# n = 0
# namber = int(input("Ishchilar sonini kiriting: "))

# while n <= namber:
#     name = input("Ismingizni kiriting: ")
#     hour = int(input("Haftalik Ish soatingizni  kiriting: "))
#     n += 1
#     if n == namber and hour <40:
#         print(f"{name} ish soatingiz juda kam ")
#         break