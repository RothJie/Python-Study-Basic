"""
工厂设计模式
"""


class Animal:
    """ 定义动物类 作为一个顶层接口, 在这个类中，写出所有的接口函数 """

    def make_sound(self):
        pass

    def eat(self):
        pass


class Dog(Animal):
    """ 所有动物都需要继承 Animal 类， 并实现中的其中的方法 """

    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    """ 所有动物都需要继承 Animal 类， 并实现中的其中的方法 """

    def make_sound(self):
        print("Meow!")


class AnimalFactory:
    """ 根据动物类创建一个工厂类, 所有类的对象创建都交给这个工厂类来完成 """

    @staticmethod
    def get_animal(animal_type):  # 利用Python中的 “鸭子类型” 或者 多态 结构
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None


# 使用工厂模式创建对象
my_pet = AnimalFactory.get_animal("dog")
my_pet.make_sound()  # 输出: Woof!
your_pet = AnimalFactory.get_animal("cat")
your_pet.make_sound()  # 输出: Meow!
