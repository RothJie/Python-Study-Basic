str_lo ="""# 文件的读写打开关闭     
# 关键在于open()函数的使用
# 传参：file、mode、encoding、newline
# file:文件路径、直接用Windows的要r""或者\\
# mode:r rb r+ w wb w+ a a+
# encoding="utf8" 不支持二进制
# read()全篇读取 readline(1) 可以读取指定行2  readlines()返回全部行组成的列表
#newline???
"""


# file= open(file=r"C:\Users\Administrator\Desktop\猜数字游戏.py",mode='r',encoding="utf-8")
# li = file.readlines()
# for i in li:
#     print(i)
# print(file.readlines())
# print([u.strip('\n') if len(u) < 20 else u for u in file.readlines() ])

# file= open(file=r"C:\Users\Administrator\Desktop\xin.txt",mode='w',encoding="utf-8")
# file.write(str_lo)
#
# file= open(file=r"C:\Users\Administrator\Desktop\xin.txt",mode='a',encoding="utf-8")
# file.write('eswtggjg')

# file= open(file=r"C:\Users\Administrator\Desktop\xin.txt",mode='ab')
# file.write(b'\x00\x01\x02\x03\x00\x01\x02\x03')
# file.close()

# with open(file=r"C:\Users\Administrator\Desktop\猜数字游戏.py",mode='r',encoding="utf-8") as fi:
#     print(fi.read())

# with open(file=r'C:\Users\Administrator\Desktop\日常办公\壁纸\睡美人.png',mode='rb') as of:
#     flu = of.read()
#     with open('auofs.png',mode='wb') as ipf:
#         ipf.write(flu)