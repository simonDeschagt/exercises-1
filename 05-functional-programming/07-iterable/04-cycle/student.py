class Cycle():
    def __init__(self,data):
        self.data = data
        self.__currentIndex = 0

    def __next__(self):
        result = self.data[self.__currentIndex]
        self.__currentIndex += 1
        if self.__currentIndex == len(self.data):
            self.__currentIndex = 0
        return result

    def __iter__(self):
        return self