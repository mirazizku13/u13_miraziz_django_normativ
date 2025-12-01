with open('numbers.txt','r') as f:
    a = f.read()
print(f"Faylda 0 raqami {a.count('0')} marta uchradi.")


juft = []
toq = []
with open('numbers.txt', 'r') as f:
    data = f.read().split()

    for i in data:
        son = int(i)
        if son%2 == 0:
            juft.append(int(i))
        else:
            toq.append(int(i))

print(f'juft: {juft}, \ntoq: {toq}')

# with open("numbers.txt") as a:
#     raqamlar = list(map(int, a.read().split()))
# total = 0
# for i in raqamlar:
#     total += i
# print(total)
# 4
# with open("numbers.txt") as a:
#     raqamlar = list(map(int, a.read().split()))
# m_son = raqamlar[0]
# for i in raqamlar:
#     if i > m_son:
#         m_son = i
# print(m_son)
# 5
# with open("numbers.txt") as a:
#     raqmlar = list(map(int, a.read().split()))
# mu_son = 0
# for i in raqmlar:
#     if i > 0:
#         mu_son += 1
# print(mu_son)
