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
