import json

# print('№1 Buyurtmalar va umumiy summa')
# print('')
# with open("les25.1.json", "r") as f:
#     data = json.load(f)
#
#
# total = 0
# for order in data["orders"]:
#     if order["status"] == "paid":
#         total += order["total_price"]
#
# print("Paid buyurtmalar jami summa:", total)
# print('')
#
# print("№2 Har bir buyurtmadagi mahsulotlar soni")
# print('')
#
# with open("les25.2.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#
#
# for order in data["orders"]:
#     total_qty = 0
#     for item in order["items"]:
#         total_qty += item["qty"]
#
#     print(f"Buyurtma {order['id']}: jami {total_qty} ta mahsulot")
# print('')
# print('№3. Talabalar va o‘rtacha ball')
# print('')
#
# with open("les25.3.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#
# for student in data["students"]:
#     grades = student["grades"]
#     sum1 = sum(grades) / len(grades)
#
#     if sum1 > 80:
#         print(f"{student['name']} - o'rtacha ball: {sum1}")
# print('')
# print('№4. Kategoriya va mahsulotlar soni')
# print('')
# with open("les25.4.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#
# for category in data["categories"]:
#     name = category["name"]
#     count = len(category["products"])
#     print(f"{name}: {count} ta mahsulot")
# print('')
# print('№5. Eng qimmat mahsulotni topish')
# print('')
# with open("les25.4.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
# max_price = 0
# expensive_product = ""
#
# for category in data["categories"]:
#     for product in category["products"]:
#         if product["price"] > max_price:
#             max_price = product["price"]
#             expensive_product = product["name"]
#
# print(f"Eng qimmat mahsulot: {expensive_product} ({max_price})")
# print('')
# print('№6. Blog foydalanuvchilari va postlar soni')
# print('')
#
# with open('les25.6.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# no_posts_users = []
# for user in data["users"]:
#     username = user["username"]
#     post_count = len(user["posts"])
#
#     print(f"{username}: {post_count} ta post")
#
#     if post_count == 0:
#         no_posts_users.append(username)
#
# print("\nPostlari yo‘q foydalanuvchilar:")
# for u in no_posts_users:
#     print("-", u)
#
# print('')
# print('7. Eng ko‘p like olgan post')
# print('')
#
# with open('les25.6.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# max_likes = -1
# best_user = ""
# best_title = ""
#
# for user in data["users"]:
#     username = user["username"]
#     for post in user["posts"]:
#         if post["likes"] > max_likes:
#             max_likes = post["likes"]
#             best_user = username
#             best_title = post["title"]
#
# print("Eng ko‘p like olgan post:")
# print("Foydalanuvchi:", best_user)
# print("Post:", best_title)
# print("Likes:", max_likes)
#
# print('')
# print('8. Kutubxona va mualliflar bo‘yicha sanash')
# print('')
# with open('les25.8.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# authors = {}
#
# for book in data["books"]:
#     author = book["author"]
#
#     if author not in authors:
#         authors[author] = 0
#
#     authors[author] += 1
#
# for author, count in authors.items():
#     print(f"{author}: {count} ta kitob")
#
# print('')
# print('9. Yil bo‘yicha eski kitoblar')
# print('')
# with open('les25.8.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# print("2000-yildan oldingi kitoblar:")
#
# for book in data["books"]:
#     if book["year"] < 2000:
#         print("-", book["title"])
# print('')
# print('10. Buyurtmadagi umumiy miqdor va summa')
# print('')
# with open('les25.10.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# total_qty = 0
# total_sum = 0
#
# for item in data["cart"]["items"]:
#     total_qty += item["qty"]
#     total_sum += item["price"] * item["qty"]
#
# print("Jami mahsulotlar soni:", total_qty)
# print("Jami umumiy summa:", total_sum, data["cart"]["currency"])
#
# print('')
# print('11. Foydalanuvchilar va ularning rollari')
# print('')
#
# with open('les25.11.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# admins = 0
# users = 0
# mods = 0
#
# for user in data["users"]:
#     if user["active"] == True:
#         role = user["role"]
#
#         if role == "admin":
#             admins += 1
#         elif role == "user":
#             users += 1
#         elif role == "moderator":
#             mods += 1
#
# print("Active adminlar soni:", admins)
# print("Active userlar soni:", users)
# print("Active moderatorlar soni:", mods)
#
# print('')
# print('12. Shaharlar va aholisi')
# print('')
# with open('less25.12.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# for country in data["countries"]:
#     country_name = country["name"]
#     total_population = 0
#
#     for city in country["cities"]:
#         total_population += city["population"]
#
#     print(f"{country_name}: {total_population}")
#
# print('')
# print('13. Filmlar va reytinglar')
# print('')
# with open('less25.13.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# filtered_movies = []
#
# for movie in data["movies"]:
#     if movie["rating"] > 8.0:
#         filtered_movies.append(movie)
#
# print("Reytingi 8.0 dan katta filmlar:")
# for m in filtered_movies:
#     print("-", m["title"])
#
# if filtered_movies:
#     oldest = filtered_movies[0]
#     for m in filtered_movies:
#         if m["year"] < oldest["year"]:
#             oldest = m
#
#     print("\nEng eski film:")
#     print(f"Title: {oldest['title']}, Year: {oldest['year']}")
#
# print('')
# print('14. Kurslar va o‘quvchilar soni')
# print('')
# with open('less25.14.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# max_students = 0
# max_course_name = ""
#
# for course in data["courses"]:
#     name = course["name"]
#     count = len(course["students"])
#
#     print(f"{name}: {count} ta o'quvchi")
#
#     if count > max_students:
#         max_students = count
#         max_course_name = name
#
# print(f"\nEng ko'p o'quvchiga ega kurs: {max_course_name} ({max_students} ta)")
#
# print('')
# print('15. Chegirmali mahsulotlarni ajratish')
# print('')
# with open('less25.15.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# print("Chegirmali mahsulotlar:")
#
# for product in data["products"]:
#     if product["discount"] > 0:
#         # yangi narxni hisoblash
#         new_price = product["price"] - product["price"] * product["discount"]
#         print(f"{product['name']}: {new_price}")
#
print('2-fayel')
print('1')
numbers = [1, 2, 3, 4, 5]
data = {
    "numbers": numbers
}
with open("numbers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print('2')
data = {
    "users": [
        {"name": "Ali", "age": 20},
        {"name": "Vali", "age": 25},
        {"name": "Gul", "age": 19}
    ]
}

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print('3')

