goal = 10000
kun = 0

while goal >= 0:
    try:
        qadam = int(input(f'{kun+1} - kun yurgan qadamingizni kiriting>>>'))
    except ValueError as e:
        print(f"xatolik{e}")
    else:
        goal -= qadam
        kun+=1

print(f'siz 10000 qadamlik maqsadingizni {kun} kunda bajardingiz')
# 
#     # print(x)
#     print(12 / 2)
# 