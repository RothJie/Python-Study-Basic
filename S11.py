
""" 单例设计模式 """


class Singleton:
    _instance = None   # 类属性，用于存储属于该类的一个实例

    def __new__(cls):      # 该魔法方法,主要用于创建实例的时候使用
        if cls._instance is None: # 找到存储该类实例的那个类属性，并判断该类属性是否有值，如果有值表示该类已经有实例对象了，就不在创建，直接引用
            cls._instance = super(Singleton, cls).__new__(cls)     # 根据 Singleton 这个类，分配内存空间
        return cls._instance

class DatabaseConnection(Singleton):
    def __init__(self):
        self.connection = "Connected to DB"

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # 输出 True，因为它们是同一个实例
