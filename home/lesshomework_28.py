# def only_positive(func):
#     def wrapper(num):
#         if num < 0:
#             return 'xato: musbat son kiriting'
#         return func(num)
#     return wrapper
#
# @only_positive
# def square(num):
#     return num ** 2
# print(square(3))
# print(square(-4))
#
# def count_calls(func):
#     count = 0
#     def calls(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'chaqirildi {count} marta')
#         return func(*args, **kwargs)
#     return calls
#
# @count_calls
# def hello():
#     print('hello')
#
# hello()
# hello()


def admin_only(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('role') != 'admin':
            return "Ruxsat yo'q! Faqat admin bajarishi mumkin!"
        return func(*args, **kwargs)
    return wrapper


@admin_only
def delete_user(user_id, **kwargs):
    print(f"Foydalanuvchi ID {user_id} muvaffaqiyatli o'chirildi.")



print(delete_user(101, role='admin'))
print(delete_user(102, role='user'))


from datetime import datetime

def time_restricted(start_hour, end_hour):
    def decorator(func):
        def wrapper():
            now = datetime.now().hour
            if not (start_hour <= now < end_hour):
                return f"Funktsiya faqat {start_hour}:00 dan {end_hour}:00 gacha ishlaydi!"
            return func()
        return wrapper
    return decorator


@time_restricted(9, 17)   # 9:00–17:00 orasida ishlaydi
def send_report():
    print("Hisobot muvaffaqiyatli yuborildi!")


print(send_report())


def call_limit(limit):
    def decorator(func):
        count = 0

        def wrapper():
            nonlocal count
            if count >= limit:
                return "Funktsiya chaqiruvlar limiti oshib ketdi!"
            count += 1
            return func()
        return wrapper
    return decorator


@call_limit(3)
def process_data():
    print("Ma'lumotlar qayta ishlanmoqda...")



process_data()
process_data()
process_data()
print(process_data())
