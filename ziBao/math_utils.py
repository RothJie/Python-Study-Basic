__all__ = ["add","multiply","divide","substract"]

def multiply(x, y):
    """ 实现一个简单的乘法计算 """ 
    return x * y

def add(x,y):
    """ 实现一个简单的加法计算 """ 
    return x+y

def substract(x, y):
    """ 实现一个简单的减法计算 """ 
    return x-y

def divide(x,y):
    """ 实现一个简单的除法计算 """ 
    if y == 0:
        return "the number of divided is not 0"
    return x / y


