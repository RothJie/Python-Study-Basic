class Person:
    """ 定义人类 """
    species = 'Human'  # 类属性

    def __init__(self, name: str, age: int):
        """ Person 类的初始化方法 """
        self.__name = name  # self.__name 表示人的姓名
        self.__age = age  # self.__age 表示人的年龄
        self.__gender = None  # self.__gender 默认值为None, 一般情况是 man or women

    def greet(self):
        """ Person 类 打招呼的实例方法 """
        print("Hello, My name is {}! I'm {}.".format(self.__name,
                                                     Person.species))  # 如果在实例方法中需要使用类属性(类名.属性名)如这里的 Person.species

    @classmethod
    def from_string(cls, info: str):  # Person 类的 类方法, 类方法是不需要实例化，就可以调用的方法
        """ 格式化一个 info 字符串，并创建Person类的对象 """
        name, age = info.split(',')
        print("Hello, My name is {}! I'm {}.".format(name, cls.species))  # 如果在类方法中需要使用类属性(cls.属性名)如这里的 cls.species
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):
        """ Person 类的静态方法，判断 是否成年了"""
        return age >= 18

    @staticmethod
    def is_male(gender: str):
        """ Person 类的静态方法，判断 是否是男性了"""
        if gender == "man":
            return True
        if gender == "women":
            return False

    def get_name(self):
        """ Person 类的 getter 方法 获取 name 信息 """
        return self.__name

    def set_name(self, name: str):
        """ Person 类的 setter 方法 获取 name 信息 """
        self.__name = name

    def get_age(self):
        """ Person 类的 getter 方法 获取 age 信息 """
        return self.__age

    def set_age(self, age: str):
        """ Person 类的 setter 方法 获取 age 信息 """
        self.__age = age

    def get_gender(self):
        """ Person 类的 getter 方法 获取 gender 信息 """
        return self.__gender

    def set_gender(self, gender: str):
        """ Person 类的 setter 方法 获取 gender 信息 """
        self.__gender = gender

    def __str__(self):
        """ Person 类的魔法方法 __str__ 用于输出Person类的对象信息 """
        return "{},{},{}".format(self.get_name(), self.get_age(), self.get_gender())

    def __len__(self):
        return len(self.__name)



if __name__ == "__main__":
    person_str = "张三,16"
    zhang_san = Person.from_string(person_str)
    print(zhang_san)
    zhang_san.set_gender("man")
    print(zhang_san)
    print("张三成年了:{}".format(Person.is_adult(zhang_san.get_age())))
    print("张三是男性:{}".format(Person.is_male(zhang_san.get_gender())))
    zhang_san.greet()

    print("=============================================================")
    xiao_wang = Person("小王", 23)
    xiao_wang.set_gender("man")
    print(xiao_wang)

    print("=============================================================")
    xiao_hua = Person("唐语花", 18)
    xiao_hua.set_gender("women")
    print(len(xiao_hua))

