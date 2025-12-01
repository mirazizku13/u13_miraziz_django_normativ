# pi_file = open('pi.txt')
# pi = pi_file.read()
# print(pi)
# pi_file.close()
# from os import write
# from os.path import split

#
# with open('pi.txt') as f:
#     pi = f.read()
#     print(pi)
# print(f.closed)



# with open('pi2.txt') as f:
#     for qator in f:
#         print(qator.strip())



# with open('pi.txt', 'w') as f:
#     f.write('hello world')
#
# with open('pi.txt', 'a') as f:
#     f.write('\nhi miraziz')
#
# pi_file = open('pi.txt')
# pi = pi_file.read()
# print(pi)
# pi_file.close()

# a = 0
# while True:
#     with open('pi.txt', 'a+') as f:
#         f.write('\nhello world')
#         f.seek(0)
#         print(f.read())
#     a+=1
#
#     if a == 10:
#         break
#     else:
#         continue
#
# data= []
# with open('pi2.txt', 'r+') as f:
#     for i in f:
#         name, ball = i.strip().split(' - ')
#         # print(name, ball)
#         if int(ball) <80:
#             ball = int(ball) + 5
#         data.append(f'{name} - {ball}')


data= []
with open('pi2.txt', 'r+') as f:
    for i in f:
        d = i.strip().split(' - ')
        # print(name, ball)
        name = d[0]
        ball = int(d[1])
        if ball <80:
            ball += 5
        data.append(f'{name} - {ball}\n')

with open('pi2.txt', 'w') as f:
    for i in data:
        f.write(i)
