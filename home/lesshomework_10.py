uz_to_eng = {
    "salom": "hello",
    "kitob": "book",
    "maktab": "school"
}

eng_to_uz = {
    "hello": "salom",
    "book": "kitob",
    "school": "maktab"
}
work = input("nima qilmoqchisiz(qoshish, topish, yangilash, ochirish, korish)")

if work == "topish":
    til = input("qaysi tilda (eng yoki uz): ")

    if til == "uz":
        soz = input("so`zni kiring o`zbekchada yoki ingliz tilida: ")
        a = uz_to_eng.get(soz)
        if a:
            print(f"qidirayotgan {soz} sozingni manolari")
            print(a)
        else:
            print("topilmadi")
    elif til == "eng":
        soz = input("so`zni kiring o`zbekchada yoki ingliz tilida: ")
        b = eng_to_uz.get(soz)
        if b:
            print(f"search {soz}")
            print(b)
        else:
            print("not search")
    else:
        print("bunaqa til yo`q")
elif work == "qoshish":
    uz = input("o`zbek tilidagini kiriting: ")
    eng = input("ingliz tilidagini kiriting: ")
    uz_to_eng.update({uz:eng})
    eng_to_uz.update({eng:uz})
    print(uz_to_eng, eng_to_uz)
elif work == "yangilash":
    print(uz_to_eng, eng_to_uz)
    d1 =input("qaysi sozni yangilamoqchisiz kalitini kiritng: ")
    
    if d1 not in uz_to_eng:
        print("bunday lugat yo`q")
    else:
        d2 =input("yangi sozni kiting: ")
        d3 = uz_to_eng.get(d1)
        eng_to_uz.pop(d3)
        uz_to_eng.update({d1:d2}) 
        eng_to_uz.update({d2:d1})
        print(uz_to_eng, eng_to_uz)


        # d2 =input("yangi sozni kiting: ")
        # d3 = uz_to_eng.get(d1)
        # eng_to_uz.pop(d3)
        # uz_to_eng.update({d1:d2}) 
        # eng_to_uz.update({d2:d1})
        # print(uz_to_eng, eng_to_uz)


elif work == "ochirish":
    print(uz_to_eng,eng_to_uz)
    dell_word = input("qaysi sozni o`chirmo`chisiz: ")

    if dell_word not in uz_to_eng:
        print("bunday lugat yo`q")
    else:
        word1 =uz_to_eng.get(dell_word)
        eng_to_uz.pop(word1)
        uz_to_eng.pop(dell_word)
        print(uz_to_eng,eng_to_uz)

elif work == "korish":
    print("O'zbekcha → Inglizcha so'zlar:")
    for uz, eng in uz_to_eng.items():
        print(f"{uz} → {eng}")

    print("\nInglizcha → O'zbekcha so'zlar:")
    for eng, uz in eng_to_uz.items():
        print(f"{eng} → {uz}")

