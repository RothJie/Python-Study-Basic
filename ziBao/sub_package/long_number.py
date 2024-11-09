from ..math_utils import *

def int_number_add(x,y):
    return add(x,y)

def float_number_add(x,y):
    return round(float(add(x,y)),3)

if __name__ == '__main__':
    int_number_add(2,5)