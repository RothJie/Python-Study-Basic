class Observer:
    def update(self, message:str)  -> None:
        pass

class NewsLetter(Observer):
    def update(self, message:str) -> None:
        print("NewsLetter received:{}".format(message))


class DataStore:
    def __init__(self) -> None:
        self._observers:list[Observer] = []
        self._data = None

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unregister_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._data)

    def set_data(self, data: str) -> None:
        self._data = data
        self.notify_observers()


data_store = DataStore()      # 利用数据 存储类创建一个用于存储信息的对象 相当于一个用户数据库
newsletter = NewsLetter()     # 创建一个新消息对象，新消息通过这个了向所有用户发送消息提示
data_store.register_observer(newsletter)  #  将有登记信息register的用户加入列表库中
data_store.set_data("New data available!") # 利用数据存储类中的set_data 方法输入新消息到库中，并通知用户