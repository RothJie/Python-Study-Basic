# print('hello','world')
# # print('H','D','c')
# print('hello world')
#
# print('hello' + 'world!')
#
# print('hello',"word",sep='565656')
# print('-'*50)
# print('+'*50)
# print('='*50)
#
# print("hao are you?",end='')
# print("hao are you?")


# print(5/2)
# print(5//2)
# print(5%2)
# print(5*2)
# print(5**2)
# print(5**3)
#
# print(5>3)
# print(5<3)
#
# print(20>11>5)
# print(20>11<6)
#
# print(20>10 and 10> 6)
#
# print(not 20>11)
#
# number = input("请输入一个你最喜欢的数字：")
# print(number)
# print(type(number))
# # print(number + 10)
# print(int(number) + 10)
# print(number + str(10))

# username0 = input('请输入用户名字：')
# print(username0)
# print('welcome',username0)
# print('welcome' + username0)


# sentence = 'tom\'s pet is a cat'
# sentence2 = "tom's pet is a cat"
# sentence3 = "tom said:\"hello world!\""
# sentence4 = 'tom said:"hello world"'
#
# print(sentence)
# print(sentence2)
# print(sentence3)
# print(sentence4)


# words = """
# hello
# world
# abcd"""
# print(words)
#
# words1 = """hello
# world
# abcd"""
#
# print(words1)
# print(3)
#
# print(words1,end='')
# print(3)

# py_str = 'python'
# print(len(py_str))
# print(py_str[0])
# print("python"[0])
# print(py_str[-1])
# print(py_str[2:4]) #包括前不包括后面的
# print(py_str[2:])
# print(py_str[:2])
# print(py_str[:])
# print(py_str[::2])
# print(py_str[::3])
# print(py_str[1::2])
#
# print(py_str[::-1]) #倒叙
# print(py_str[::-2])

# print(py_str + ' is good')
# print(py_str * 3)

# print('t' in py_str)
# print('th' in py_str)
# print('to' in py_str)
# print('to' not in py_str)

# # 列表操作
# alist = [10, 20, 30, 'bob', 'alice', [1,2,3]]
# print(len(alist))
# print(alist[-1])
# print(alist[-1][-1])
# print(alist[-2][2])
# print(alist[3:5])
# print(20 in alist)
# print('o' in alist)
# print(100 not in alist)
# print( alist[-1] == 100)
# alist.append(899)
# alist[0] = alist[0]*alist[2]
# print(alist)


# # 元组操作
# tuple1 = (10, 20, 30, 'bob', 'alice', [1,2,3])
# print(len(tuple1))
# print(tuple1[0])
# print(tuple1[3:5])

# # 字典操作
# adict = {'name': 'bob', 'age': 23,'姓名': '李二狗','学号':'001'}
# print(len(adict))
# print('name' in adict)
# adict['邮箱'] = '3110711143@qq.com'
# adict['age'] = 25
# del adict['姓名']
# adict.pop('学号')
# print(adict)

# # 条件判断和三元运算
# m = 8
# n = 9
# s = m if m < n else n
# print(s)
#
# if m< n :
#     s = m
#     print(s)
# else:
#     s = n
#     print(s)

# # 用户登录检测
# import getpass
#
# usermame = input("Enter your name: ")
# password = getpass.getpass('Enter your password: ') #密码保护
#
# if usermame == 'W' and password == '123456':
#     print("Welcome " + usermame+ '!')
# else:
#     print('登录失败！请检查用户名和密码是否正确')
#

# # 猜数字游戏
# import random
# import time
#
# while True:
#     words = input('游戏请输入Y/退出请输入N：')
#     w = 0
#     T = 6
#     if words == 'Y' or words == 'y':
#         a = random.randint(1, 100)
#         while True:
#             b = int(input("请输入你喜欢的数字(挑战次数为6次，数字范围为1~100之间的数字): "))
#             w += 1
#             if a == b:
#                 print('恭喜你，猜对了！')
#                 print('哦那，恭喜你！ 才{}次就猜对了哦！厉害厉害，请收下我的膝盖！'.format(w))
#                 print('6'*80,end='\n\n')
#                 break
#             elif a > b and w < T:
#                 print('不对哦，你猜小了！')
#                 print('哦那，恭喜你！已经猜了{}次了哦！还有{}次哦！'.format(w, T-w))
#                 print('~' * 50,end='\n\n')
#             elif a < b and w < T:
#                 print('不对哦，你猜大了！')
#                 print('哦那，恭喜你！已经猜了{}次了哦！还有{}次哦！'.format(w, T-w))
#                 print('~' * 50,end='\n\n')
#             else:
#                 print('250???很遗憾！挑战次数已用完了！')
#                 time.sleep(5)
#                 print('世界毁灭了，本次游戏该结束了！')
#                 print('='*50,end='\n\n')
#                 break
#
#     elif words == 'N' or words == 'n':
#         print('已退出游戏！')
#         print('*' * 50,end='\n\n')
#         break
#
#     else:
#         print('请输入Y or N？已退出游戏！')
#         print('*' * 50,end='\n\n')
#         break

# while True:
#     score = int(input("Enter your score: "))
#     if score >= 90:
#         print("优秀")
#         print('\n')
#     elif score >= 80:
#         print('良好')
#         print('\n')
#     elif score >= 60:
#         print('中等')
#         print('\n')
#     else:
#         print('你该努力了？？？')


# 猜拳
# import random
#
# li = ['石头','剪刀','布']
#
# while True:
#     computer = random.choice(li)
#     player = input('这是猜拳游戏，请出，加油！：')
#     print("you choice:%s,computer:%s"%(player,computer),end='\n')
#     if player == '石头':
#         if computer == '石头':
#             print('我们都一样，平局！')
#             print('-' * 50, end='\n\n')
#         elif computer == '剪刀':
#             print('你赢了，真棒！加油加油！')
#             print('=' * 50, end='\n\n')
#         else:
#             print('很遗憾！you are looser!')
#             print('~' * 50, end='\n\n')
#     elif player == '剪刀':
#         if computer == '石头':
#             print('很遗憾！you are looser!')
#             print('~' * 50, end='\n\n')
#         elif computer == '剪刀':
#             print('我们都一样，平局！')
#             print('-' * 50, end='\n\n')
#         else:
#             print('你赢了，真棒！加油加油！')
#             print('=' * 50, end='\n\n')
#     elif player == '布':
#         if computer == '石头':
#             print('你赢了，真棒！加油加油！')
#             print('=' * 50, end='\n\n')
#         elif computer == '剪刀':
#             print('很遗憾！you are looser!')
#             print('~' * 50, end='\n\n')
#         else:
#             print('我们都一样，平局！')
#             print('-' * 50, end='\n\n')
#     else:
#         break

# import random
# all_choices = ['石头', '剪刀', '布']
# play_win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# while True:
#     p = input("""让我们开始猜拳游戏吧--------->
# (1) 石头
# (2) 剪刀
# (3) 布
# 请输入 (1/2/3): """)
#     computer_choice = random.choice(all_choices)
#     player = all_choices[int(p)-1]
#     print("玩家:%s,电脑:%s"%(player,computer_choice),end='\n')
#     if computer_choice == player:
#         print('\033[31;1m平局\033[0m',end='\n\n')
#     elif [player,computer_choice] in play_win_list:
#         print('\033[32;1m赢了，玩家终于赢得了此次比赛的冠军！！！\033[0m',end='\n\n')
#     else:
#         print('\033[33;1m玩家输了，YOU LOSE???\033[0m',end='\n\n')


# # 猜数字游戏改良加强版
# import random
#
# dif = input("""(1) 初级难度
# (2) 高级难度
# (3) 地狱级难度
# 请输入挑战难度（1/2/3）：
# """)
#
# def game_core(dif_tu:list):
#     num = random.randint(dif_tu[1][0], dif_tu[1][1])
#     counter = 0
#     while counter < dif_tu[0]:
#         answer = int(input('请留下你最喜欢的数字: '))
#         if answer > num:
#             print('不对哦，猜大了!')
#             print('~' * 50)
#         elif answer < num:
#             print('不对哦，你猜小了！')
#             print('~' * 50)
#         else:
#             print('恭喜你，猜对了！')
#             print('哦那，恭喜你！ 才{}次就猜对了哦！厉害厉害，请收下我的膝盖！'.format(counter))
#             print('6'*80,end='\n\n')
#             break
#
#         counter += 1
#         print('\033[33;1m这是第{}次，还有{}机会！\033[0m'.format(counter,dif_tu[0]-counter),end='\n\n')
#     else:
#         print('这个数字是:', num)
#
# if __name__ == '__main__':
#     if int(dif) == 1:
#         print('你已进入初级难度！')
#         dif_tup = [6, (0, 100)]
#         print('本次猜数字挑战共有{}次机会，猜数字的范围为{}，加油，相信你会成功的！'.format(dif_tup[0], dif_tup[1]))
#         game_core(dif_tup)
#     elif int(dif) == 2:
#         print('你已进入高级难度')
#         dif_tup = [8, (0, 999)]
#         print('本次猜数字挑战共有{}次机会，猜数字的范围为{}，加油，相信你会成功的！'.format(dif_tup[0], dif_tup[1]))
#         game_core(dif_tup)
#     else:
#         print('你已进入地狱级难度！')
#         dif_tup = [15, (0, 8888)]
#         print('本次猜数字挑战共有{}次机会，猜数字的范围为{}，加油，相信你会成功的！'.format(dif_tup[0], dif_tup[1]))
#         game_core(dif_tup)

total = 0
i= 1 
while i<101:
    total += i
    i = i+1
print(total)

