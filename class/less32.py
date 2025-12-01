# sonlar1 = [1,2,3,4,5]
#
# sonlar = iter(sonlar1)
# print(next(sonlar)) #1
# print(next(sonlar)) #2
# print(next(sonlar))#3
# print(next(sonlar))#4
# print(next(sonlar))#5
# # print(next(sonlar)) #xato(StopIteration)
# print()
# for i in sonlar1:
#     print(i)
class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Unversitet:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.talabalar = []

    def __iter__(self):
        return iter(self.talabalar)

    def __next__(self):
        pass
t1 = Talaba("ALi", 20)
t2 = Talaba("Vali", 21)
t3 = Talaba("Gani", 23)

u1 = Unversitet("TATU", "YUNSOBOD")

u1.talaba= [t1, t2, t3]

# for i in u1:
#     print(i.name)

# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current>= self.end:
#             raise StopIteration
#         self.current +=1
#         return self.current -1
#
# for i in MyIterator(1,10):
#     print(i)


def yrange(n):
    i = 0
    while i<n:
        yield i
        i +=1
        # return i
a = yrange(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))