from typing import Union

# 圆周长
def yuan_L(r:Union[str,float,int]):
    return 2*3.14*float(r)

# 圆面积
def yuan_S(r:Union[str,float,int]):
    r = float(r)
    return 3.14*r**2

# 定义可以计算圆周长和面积的函数
def get_yuan_info(r:Union[str,float,int]):
    return [yuan_L(r),yuan_S(r)]

print(get_yuan_info(3))
print(get_yuan_info(3.23))
print(get_yuan_info('1'))


