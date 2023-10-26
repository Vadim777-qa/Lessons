# mro - method resolution order - путь с помощью которого мы узнаем кто с родительских классов старше
class Animal:
    def live(self):
        pass


class Tiger(Animal):
    def live(self):
        pass


print(Tiger.__mro__)
