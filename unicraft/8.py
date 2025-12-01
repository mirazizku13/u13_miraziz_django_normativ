products = {
    "adrenaline": {"narxi": 200, "soni":20},
    "coca-cola": {"narxi": 10000, "soni":30},
    "morojniy": {"narxi": 20000, "soni":10},
    "non": {"narxi": 50000, "soni":200},
}


def mahsulot_qoshish():
    nom = input("Mahsulot nomini kiring: ").lower()
    try: 
        narxi = int(input("mahsulot narxini kiriting: "))
        soni = int(input("mahsulot soni: "))
        if narxi<=0 or soni <=0:
            print("Xatolik: narxi va soni 0 dan katta bo`lshi kerak.")
            return
    except ValueError as e:
        print(e,"Xatolik: faqat butun son kiriting.")
        return
    
    if nom in products:
        products[nom]["soni"] +=soni
        print(f"{nom} bazada bor, soni{soni} ta")
    else:
        products[nom] = {'narxi': narxi, "soni": {soni}}
        print(f"Yangi mahsulot qo`shiildi: {nom} - narxi {narxi}, soni {soni}")
    
def mahsulot_olib_chiqish():
    nom = input("Mahsulot nomini kiring: ").lower()
    
    miqdor = int(input("olish miqdorini kiring: "))
    if miqdor <=0:
        print("Xatolik: miqdor 0 dan katta bo`lshi kerak. ")  
        return
    if nom not in products:
        print("Mahsulot topilmadi")
        return
        
    
    obmor = products[nom]["soni"]
    if obmor < miqdor:
        print(f"Zaxirada yetarli emas. omborda: {obmor} dona bor")
    elif obmor == 0:
        print("omborhonada qolmagan")
    else:
        products[nom]["soni"]-= miqdor
        print(f"{nom} dan {miqdor} dona olindi")


def mahsulotlar_royhati():
    if not products:
        print("Omborhona bo`sh yani hech narsa yo`q")
        return
    print("---------------------ombor honadagi mahsulotlar---------------------------")
    print(f"{"nomi"} {"narxi"} {"soni"}{ "jami"}")

    for nom, info in products.items():
        narx = info["narxi"]
        soni = info["soni"]
        jami = narx * soni
        print(f"nomi: {nom},    narxi: {narx},    soni: {soni},    jami: {jami}")


def main():
    while True:
        try:
            a = int(input(f"1.mahsulotni qoshish\n2.mahsulotni olib chiqish\n3.mahsulotniroyhati\n0.exit\nnima qilasiz:"))
            if a == 0:
                print("xayir salomat bo`ling")
                break
            elif a == 1:
                mahsulot_qoshish()
            elif a == 2:
                mahsulot_olib_chiqish()
            elif a ==3:
                mahsulotlar_royhati()
        except ValueError as a:
            print(a,"")           
main()





# #sklad sistemasi

# products={
#     'Gorilla':{"narxi":10000,"soni":50},
#     'Pepsi':{"narxi":15000,"soni":100},
#     'Snikers':{"narxi":8000,"soni":150},
#     'Prizidend saryog':{"narxi":40000,"soni":80},
# }
# def add_product():
#     nom=input("Mahsulot nomini kriting>>>").strip().lower()
#     try:
#          narxi =int(input("Narxini kriting>>>"))
#          soni=int(input("Soniini kriting>>>"))
#          if narxi<=0 or soni<=0:
#              print("Xatolik:Narx va son 0 dan katta bilishi kerak.")
#              return
#     except ValueError:
#          print("Narx va son butun son bolishi kerak.")
#          return
#     if nom in products:
#          products[nom]['narxi'] += soni
#          print(f"{nom} yangilandi.Umumiy:{products[nom]['soni']} dona")
#     else:
#              products[nom]={'narxi':narxi,'soni:':soni}
#              print(f"{nom} Skladga qoshildi")
# #add_product()

# def out_product():
#     nom = input("Mahsulot nomini kriting>>>").strip().lower()
#     if nom not in products:
#         print('Mahsulot yoq')
#         return
#     try:
#         miqdor=int(input("Miqdorini kriting>>>"))
#         if miqdor<=0:
#             print("Miqdor 0 dan katta bolishi kerak.")
#             return
#     except ValueError:
#         print("Miqdor butun son bolishi kerak.")
#         return
#     avieble=products[nom]['soni']
#     if avieble<miqdor:
#         print("Mahsulot yetarli emas")
#     else:
#         products[nom]['soni']-=miqdor
#         print(f"Ok qoldi:{products[nom]['soni']} dona")
# #out_product()
# def menu_products():
#     if not products:
#         print("Sklad bosh")
#         return
#     print("--------Sklad menyusi--------")
#     print(f"{nomi},{narxi},{soni},{umumiy}")
#     for k,v in products.items():
#         narxi=v['narxi']
#         soni=v['soni']
#         umumiy= narxi*soni
#         print(f"nomi:{nomi}, {narxi}:narxi,{soni}:soni,{umumiy}:umumiy")
# #menu_products()
# def main():
#     while True:
#         a=int(input(f"1.mahsulot qoshish\n2.mahsulot olib ciqish\n3.mahsulot royxati\n0.exit\n nima qilasiz"))
#         if a==0:
#             break
#         elif a==1:
#             add_product()
#         elif a==2:
#             out_product()
#         elif a==3:
#             menu_products()
# main()
