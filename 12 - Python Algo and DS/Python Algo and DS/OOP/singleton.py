class TheSingleton:
    __instance = None
    name = None

    @staticmethod
    def getInstance():
        if not TheSingleton.__instance:
            TheSingleton()
        return TheSingleton.__instance

    def __init__(self):
        TheSingleton.__instance = self

    def getName(self):
        return TheSingleton.name

class Singleton:
    __instance = None
    name = None

    @staticmethod
    def getInstance(name):
        if Singleton.__instance:
            return Singleton.__instance
        return Singleton(name)

    def __init__(self, name):
        Singleton.__instance = self
        Singleton.name = name

leObject = Singleton.getInstance("Metallica")
print(leObject.name)
leObject.getInstance("John")
print(leObject.name)