bosh_toplam = set()

a = {1,2,3,4,5,6,7,8,9,10}
d = bosh_toplam.union(a)
print(d)
bosh_toplam.discard(5)
print(bosh_toplam)

a1 = {1,2,3,4,5}
a2 = {4,5,6,7,8}

d = a1.union(a2)
print(d)
d2 = a1.intersection(a2)
print(d2)

farqi = a1.difference(a2)
print("Farqi:", farqi)

print(a1 == a2)
a3 = {2,3,4}
a4 = {2,3,4}
print(a3 == a4)