class PadZip():
    def __init__(self, data1, data2, padding=None):
        self.data1 = data1
        self.data2 = data2
        self.padding = padding
        self.__currentIndex = 0

    def __next__(self):
        # print(self.data1)
        # print(type(self.data1))
        if len(self.data1) > len(self.data2):
            limiter = len(self.data2)
            end_limit = len(self.data1)
        else:
            limiter = len(self.data1)
            end_limit = len(self.data2)

        if self.__currentIndex == end_limit:
            raise StopIteration()
        elif self.__currentIndex >= limiter:
            try:
                result = (self.data1[self.__currentIndex], self.padding)
            except IndexError:
                result = (self.padding, self.data2[self.__currentIndex])
        else:
            result = (self.data1[self.__currentIndex], self.data2[self.__currentIndex])

        self.__currentIndex += 1
        return result

    def __iter__(self):
        return self
    
zip = PadZip('a', [])
print(list(zip))