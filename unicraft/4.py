sonlar = [2, 3, 2 ,5, 4, 2, 5, 3, 3]
son = sonlar[0]
for i in sonlar:
    if son <i:
        son = i 
print("max son",son)

total =0
for i in sonlar:
    total += i 
print("min son",total)

total = 0
for i in sonlar:
    total += i
print("sum ",total)
'''
print(sum(sonlar))
'''


for i in range(1,10):
    print(" ")
    print(i + 0)
    print(" ")
    for j in range(2,10):
        print(f"{i} x {j} = {j * i}")
    