talaba_baholari = {
    "Ali": {"Matematika": 5, "Ingliz tili": 4},
    "Vali": {"Matematika": 2, "Ingliz tili": 2},
    "Zuhra": {"Matematika": 5, "Ingliz tili": 5},
    "Olim": {"Matematika": 2, "Ingliz tili": 2}
}

talaba_baholari["Alisher"] = {"Matematika" :3, "Ingliz tili": 5}
print(talaba_baholari["Alisher"])

talaba_baholari.pop("Olim")
print(talaba_baholari)

for k,v in talaba_baholari.items():
    print(f"{k}:{v}")

a = input("ismini kiring: ")
b = input("fanni kiring: ")
d = input("bahosini kiring: ")

talaba_baholari[a][b] = d
print(talaba_baholari[a])
ortacha ={}
for k,v in talaba_baholari.items():
    a = ((talaba_baholari[k]["Matematika"]+ talaba_baholari["Ali"]["Ingliz tili"])/len(talaba_baholari[k]))
    ortacha[k] = a
print(ortacha)

for i,e in ortacha.items():
    if e > 3:
        print(f"{i}:{e}")