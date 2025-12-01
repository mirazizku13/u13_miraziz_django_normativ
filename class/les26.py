
#
# data = [
#     {"Ism": "Ali", "yosh": 18, "Fan": "Matematika", "Baho": 5},
#     {"Ism": "Vali", "yosh": 17, "Fan": "Ingliz tili", "Baho": 4},
#     {"Ism": "Gani", "yosh": 16, "Fan": "Fizika", "Baho": 5},
#     {"Ism": "Olim", "yosh": 15, "Fan": "Matematika", "Baho": 3},
# ]
# with open("students.csv", "w", encoding="utf8", newline="") as f:
#     fildnames = ["Ism", "yosh", "Fan", "Baho"]
#     writer = csv.DictWriter(f, fieldnames=fildnames)
#     writer.writeheader()
#     writer.writerows(data)
# with open("students.csv", encoding="utf8", newline="") as f:
#     reader = csv.DictReader(f)
#     ages = [int(row["yosh"]) for row in reader]
# print("yoshlarning ortacasi", sum(ages) / len(ages))
# fan = input("Qays fan>>")
# with open("students.csv", newline="", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row["Fan"] == fan:
#             print(row["Ism"], row["Baho"])
# with open("students.csv", newline="", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     data = list(reader)
# yangi = {
#     "Ism": input("Ism>>"),
#     "yosh": input("yosh>>"),
#     "Fan": input("Fan>>"),
#     "Baho": input("Baho>>"),
# }
# data.append(yangi)
# with open("students.csv", "w", encoding="utf-8", newline="") as f:
#     fieldnames = ["Ism", "yosh", "Fan", "Baho"]
#     writer = csv.DictWriter(f, fieldnames=fildnames)
#     writer.writeheader()
#     writer.writerows(data)
# print("Qoshildi")



import csv

# from home.lesshomework_3 import total

# with open("talaba.csv",'r', newline="", encoding="utf-8") as f:
#     red = csv.DictReader(f)
#     ages = []
#     for i in red:
#         # print(i)
#         ages.append(int(i['age']))
#     print(sum(ages)/len(ages))


# with open('talaba.csv') as f:
#     reader = csv.reader(f)
#     total = 0
#     for index, i in enumerate(reader):
#         print(index,i)
#         if index == 0:
#             continue
#         total += int(i[1])
#     print(total / index)

fan = input("Qays fan>>")
with open("talaba.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Fan"] == fan:
            print(row["Ism"], row["Baho"])
with open("talaba.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
yangi = {
    "Ism": input("Ism>>"),
    "yosh": input("yosh>>"),
    "Fan": input("Fan>>"),
    "Baho": input("Baho>>"),
}
data.append(yangi)
# with open("talaba.csv", "w", encoding="utf-8", newline="") as f:
#     fieldnames = ["Ism", "yosh", "Fan", "Baho"]
#     writer = csv.DictWriter(f, fieldnames=fildnames)
#     writer.writeheader()
#     writer.writerows(data)
# print("Qoshildi")