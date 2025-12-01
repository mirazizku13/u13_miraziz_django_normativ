# from product import mahsulot_qoshish,mahsulot_olib_chiqish,mahsulotlar_royhati


# def main():
#     while True:
#         try:
#             a = int(input(f"1.mahsulotni qoshish\n2.mahsulotni olib chiqish\n3.mahsulotniroyhati\n0.exit\nnima qilasiz:"))
#             if a == 0:
#                 print("xayir salomat bo`ling")
#                 break
#             elif a == 1:
#                 mahsulot_qoshish()
#             elif a == 2:
#                 mahsulot_olib_chiqish()
#             elif a ==3:
#                 mahsulotlar_royhati()
#         except ValueError as a:
#             print(a,"")           
# main()
import math
from datetime import datetime

now = datetime.now()
bithday = datetime(2025, 12, 31, 23)
print(now-bithday)
