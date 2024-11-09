from typing import Union


class Calculator:
    """ 定义计算器类 """

    @staticmethod
    def add(*args: Union[float, int], **kwargs: Union[float, int]) -> float:
        """ 定义一个通用的加法计算方法 """
        rsl = sum(args)
        #for k in kwargs:
        #    rsl += kwargs.get(k)
        rsl += sum(kwargs.values())
        return round(float(rsl), 2)

    @staticmethod
    def substract(a: Union[int, float], b: Union[int, float]) -> float:
        """ 定义一个通用的减法计算方法 """
        return round(float(a-b), 2)

    @staticmethod
    def multiply(*args: Union[float, int], **kwargs: Union[float, int]) -> float:
        """ 定义一个通用的乘法计算方法 """
        rsl = 1
        for u in args:
            rsl *= u
        for k in kwargs:
            rsl *= kwargs.get(k)
        return round(float(rsl), 2)

    @staticmethod
    def division(a: Union[int, float], b: Union[int, float]) -> float:
        """ 定义一个通用的除法计算方法 """
        rsl = None
        try:
            # 如果数据在转换成浮点数的时候出现错误，那么说明该数据并不是 不是数数字,直接抛出 ValueError
            #如果被除数等于0，那么则抛出 ZeroDivisionError
            rsl = float(a) / float(b)
            rsl = round(rsl, 2)
        except ZeroDivisionError as e:
            print("除0错误")
        except ValueError as e:
            print("数据有误")
        finally:
            return rsl


if __name__ == "__main__":
    g = Calculator()
    print(g.add(5,6))
    print(g.add(5,6,l=9,m=8))
    print(g.substract(5,4))
    print(g.multiply(5,4,l=9,m=8))
    print(g.division(9,3))

