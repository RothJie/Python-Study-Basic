# # 需求2: 使用while循环获取列表中的第一个数字的位置
# li = ["89", "ss", None, False, "hello world", True, 3.14, True, 3, 90, 78]
# idx = 0
# while idx < len(li):
#     if type(li[idx]) == int or type(li[idx]) == float:
#         print("li 中第一个数字所在位置的索引是:{}, 这个数字是:{} ".format(idx, li[idx]))
#         break
#     idx += 1
# else:
#     print("li 中不存在 数字")

# 需求3: 统计列表中是数字或者是字符串数字的个数(while)
def is_float(value):    # 定义函数
    """用于判断一个字符串是不是浮点数"""
    try:
        float(value)  # 尝试将字符串转换为浮点数
        return True  # 如果转换成功，返回True
    except ValueError:
        return False  # 如果转换失败，返回False

lis = ["23", "psl", "lo", "he", "88.3", 23, 90, 2.45, 9.08, None, "true", False, True]
digit_li = []
idn = 0
while idn < len(lis):
    u = lis[idn]
    if type(u) == None or type(u) == bool:
        idn += 1
        continue
    if type(u) == int or type(u) == float:
        digit_li.append(u)
    if type(u) == str and (u.isdigit() or is_float(u)):
        digit_li.append(u)
    idn += 1
else:
    print(digit_li)
    print(len(digit_li))