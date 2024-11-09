def add_v4(**kwargs):
    """
    实现加法的第四个版本
		使用 ** 前缀修饰一个变量，并将整体作为参数，这个变量本质是一个字典
    	kwargs 可以不用叫做这个名，但是本质都是一个字典
    """
    rsl = 0
    for k in kwargs:
        rsl += kwargs[k]
    return rsl
di = {'v':10,'k':20}

print(add_v4(**di))

def add_v4(*kwargs):
    """
    实现加法的第四个版本
		使用 ** 前缀修饰一个变量，并将整体作为参数，这个变量本质是一个字典
    	kwargs 可以不用叫做这个名，但是本质都是一个字典
    """
    rsl = 0
    for k in kwargs:
        rsl += k
    return rsl
# di = {'v':10,'k':20}
dii = (10,52)
print(add_v4(*dii))