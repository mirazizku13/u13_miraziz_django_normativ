# def decor2(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return wrapper
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#
#     return wrapper
# @decor2
# @decor
# def num():
#     return 10
#
# def num2():
#     return 10
# @decor
# @decor2
# # print(num())
# print(num2())


def split(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.split(' ')
    return wrapper

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper
@split
@uppercase_decorator
def salom_ber(message):
    return f"salom {message}"

print(salom_ber("miraziz"))