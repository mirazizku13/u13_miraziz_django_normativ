'''
1️⃣ Boshlang‘ich ma’lumot (tayyor dict)
   ```python
   students = {
       "student1": {"name": "Ali", "age": 20, "grade": "B"},
       "student2": {"name": "Laylo", "age": 22, "grade": "A"},
       "student3": {"name": "Sardor", "age": 19, "grade": "C"}
   }
2️⃣ Bitta elementni yangilash
• "student2" ichidagi "grade" qiymatini "A+" ga o‘zgartiring.
• .update() yoki to‘g‘ridan-to‘g‘ri students["student2"]["grade"] = "A+" usulidan foydalaning.

3️⃣ Yangi kalit qo‘shish (nested darajada)
• "student3" ichiga "city": "Tashkent" nomli yangi juftlik qo‘shing.
• .update() metodidan foydalaning.

4️⃣ Yangi talaba qo‘shish (tashqi darajada)
• "student4" nomli yangi kalit yarating, qiymati dictionary bo‘lsin:
python {"name": "Malika", "age": 21, "grade": "B", "city": "Fergana"}

5️⃣ Ma’lumotni chiqarish
• Hamma talabalarni for sikl orqali chiqaring:
Talaba: Ali, Yosh: 20, Bahosi: B ...

6️⃣ .update() orqali bir nechta qiymatni bir vaqtning o‘zida yangilash
• "student1" uchun: {"grade": "A", "city": "Andijan"} ni .update() bilan yangilang.

7️⃣ O‘zgartirishdan oldingi va keyingi holatni solishtiring.
• Yangilanishdan oldin va keyin print(students) qilib farqni ko‘ring.
'''




students = {
    "student1": {"name": "Ali", "age": 20, "grade": "B"},
    "student2": {"name": "Laylo", "age": 22, "grade": "A"},       
    "student3": {"name": "Sardor", "age": 19, "grade": "C"}
}


students["student2"]["grade"] = "A+"

students["student1"].update({"grade": "B+"})



students["student3"].update({"city": "tashkent"})

students["student4"] = {"name": "Malika", "age": 21, "grade": "B", "city": "Fargona"}

students["student2"].update({"grade": "A", "city": "Andijon"})
for student in students.values():
    print(f"Talaba: {student["name"]}, yosh: {student["age"]}, bahosi: {student["grade"]}")
    if "city" in student:
        print(f"shahar: {student["city"]}")


