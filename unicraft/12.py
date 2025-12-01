with open('12.txt', 'r') as f:
    pi = f.read()
    print(pi)
print(f.closed)


data= []
with open('12.txt', 'r+') as f:
    for i in f:
        d = i.strip().split(' - ')
        # print(name, ball)
        name = d[0]
        ball = int(d[1])
        if ball <80:
            ball += 5
        data.append(f'{name} - {ball}\n')

with open('12.txt', 'w') as f:
    for i in data:
        f.write(i)