class InclusiveRangeIterator():
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    def __next__(self):
        if self.__first > self.__last:
            raise StopIteration()
        result = self.__first
        self.__first +=1
        return result

    def __iter__(self):
        return self
    
class InclusiveRange():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return InclusiveRangeIterator(self.first, self.last)

for x in InclusiveRange(1,5):
    print(x)