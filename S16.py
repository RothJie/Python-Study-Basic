li = [32, 32, 89, 12, 34, 1, 2, 3, 4, 78, 99, 66]
square_li = [u ** 3 for u in li if u < 10]
square_li1 = [u ** 3 if u < 10 else u ** 2 for u in li]
square_l1 = [u ** 2 if u > 32 else u ** 3 for u in li]
print(square_li1)

str_li = ["*" * (12 - u) if u <= 6 else "*" * u for u in range(12)]
for i in str_li:
    print(i)

# 双For遍历
tt = [[u for u in range(1, row + 1)] for row in range(1, 4)]
for t in tt:
    print(t)

er_wei_arr = [
    [1, 9, 20],
    [32, 11, 3],
    [34, 78, 5]
]

print([[e ** 3 if e < 10 else e ** 2 for e in row] for row in er_wei_arr])

shan_wei_arr = [
    ["12342", "34814", "39361", "44637", "14913"],
    ["12342", "34814", "39361", "44637", "14913"],
    ["12342", "34814", "39361", "44637", "14913"]
]

print([[[int(u) ** 3 if int(u) < 5 else int(u) ** 2 for u in uni] for uni in row] for row in shan_wei_arr])

san_jiao_xing = [[2, 10], [12, 23], [89, 34]]
dic = [{"x":x, "y":y} for x, y in san_jiao_xing]
print(dic)

lis = ["a",'b','c','d']
my_dict = {x: lis[x] for x in range(4)}
print(my_dict)

print({idx:uni for idx, uni in enumerate(["12", "a", "bu", "23", "x", "y"])})


li1 = ["12", "34", "32"]
li2 = ["12", "34", "32"]
li3 = ["12", "34", "32"]

print(li1+li2+li3)

li1.extend(li2)
li1.extend(li3)
print(li1)