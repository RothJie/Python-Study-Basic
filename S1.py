# 在定义一个函数的时候，可能有一个或者多个参数，也可能没有参数。
def add(n1, n2):
    return n1+n2
"""
以这个实现加法需求的函数为例，我们可以做哪些优化呢？
1.参数需要传入什么类型的参数进行计算，调用者是不知道的
2.如果需要计算多个值，而不仅仅是2个值，应该怎么办？
3.缺乏必要的描述，讲清楚这个函数是干什么的？
4.参数的默认值，对于调用者来说，是不知道的
"""

def add_v1(n1:int, n2:int) -> int:   # 注明 n1 和 n2 参数的类型是int,返回值的类型也是int
    """实现加法的第一个版本"""          # 使用三引号写出注释，注明这个函数的用法
    return n1+n2

def add_v2(n1:int=60, n2:int=60) -> int:   # 注明了每个参数的数据类型和默认值
    """实现加法的第二个版本"""
    return n1+n2

# 那么，怎么解决参数个数的问题呢？
# 对于加法运算来说，由于调用者在传入的参数个数不确定，所以可以使用不定长参数来传参
def add_v3(*args) -> int:
    """
    实现加法的第三个版本
    	使用 * 前缀修饰一个变量，并将整体作为参数，这个变量本质是一个元组
    	args 也可以不叫这个名，但是本质都是一个元组
    	可以使用内置的sum方式直接对不定长参数直接求和
    """
    rsl = 0
    for u in args:
        rsl += u
    return rsl

# 对于第三个版本的调用
result = add_v3(1, 2, 4)
print(result)

result = add_v3(11, 24, 4, 90, 12)
print(result)


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

# 对于第四个版本的函数调用方式
result = add_v4(a=10, b=20, c=30)
print(result)
result = add_v4(x=3, y=4, c=6)
print(result)


def add_v5(*args, **kwargs) -> int:
    """
    实现加法的第五个版本
    	使用 *args 和 **kwargs 进行组合使用，可以传入参数的方式可以更丰富一些,
    	需要注意的是：
    	     * 修饰的变量必须在 ** 修饰的变量的前面
    """
    rsl = 0
    for u in args:
        rsl += u
    for k in kwargs:
        rsl += kwargs[k]
    return rsl

# 对于第五个版本的函数调用方式
result = add_v5(1, 3, 5)
print(result)
result = add_v5(x=3, y=4, c=6)
print(result)
result = add_v5(2, 3, 5, b=20, c=30)
print(result)

def add_v6(n1:int=23, n2:int=23, *args, **kwargs) -> int:
    """
    实现加法的第六个版本
    	使用 *args 和 **kwargs 进行组合使用，可以传入参数的方式可以更丰富一些,
    	需要注意的是：
    	     * 修饰的变量必须在 ** 修饰的变量的前面
    """
    rsl = 0
    rsl += n1
    rsl += n2
    for u in args:
        rsl += u
    for k in kwargs:
        rsl += kwargs[k]
    print("n1={}, n2={}, args={}, kwargs={}".format(n1, n2, args, kwargs))
    return rsl

# 对于第六个版本的函数调用方式
result = add_v6(1, 3, 5, 23, 24) # n1 获取到的值是1, n2 获取到的值是3, args=(5, 23, 24,)
print(result)
result = add_v6(1, 3, x=3, y=4)  # n1 获取到的值是1, n2 获取到的值是3, kwargs={x=3, y=4}
print(result)
result = add_v6(1, 3, 2, 3, 5, b=20, c=30)  # n1 获取到的值是1, n2 获取到的值是3
print(result)                               # args=(2,3,5,)  kwargs={b=20, c=30}




