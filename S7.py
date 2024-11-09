
# # 需求1: 检查字符串中是否存在数字
# st = "lpplt90lllssso"
# for u in st:
#     if u.isdigit():
#         print("字符串中存在数字" + '{}'.format(u))
#         break
# else:
#     print("字符串中没有数字")


# 需求3: 统计列表中是数字或者是字符串数字的个数(for)
def is_float(value):    # 定义函数
    """用于判断一个字符串是不是浮点数"""
    try:
        float(value)  # 尝试将字符串转换为浮点数
        return True  # 如果转换成功，返回True
    except ValueError:
        return False  # 如果转换失败，返回False

lis = ["23", "psl", "lo", "he", "88.3", 23, 90, 2.45, 9.08, None, "true", False, True]
digit_li = []
for u in lis:
    if type(u) == None or type(u) == bool:
        continue
    if type(u) == int or type(u) == float:
        digit_li.append(u)
    if type(u) == str and (u.isdigit() or is_float(u)):
        digit_li.append(u)
else:
    print(digit_li)
    print(len(digit_li))