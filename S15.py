class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """
        这个是python类的eq方法
        :param other:
        :return:
        """
        if isinstance(other, Person): # isinstance作用：判断该other是否属于Person类对象
            return self.name == other.name
        return False

    def __ne__(self, other):
        return not self == other

# 使用__eq__和__ne__
person1 = Person("Alice")
print(person1)
person2 = Person( person1)
print(person2)
person3 = Person("Bob")
print(person1 == person2)  # 输出: False
print(person1 != person3)  # 输出: True



p = Person('j')
print(p.__dir__())
print(p.__dict__.__doc__)
