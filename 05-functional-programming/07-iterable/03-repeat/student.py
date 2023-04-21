class Repeat():
    def __init__(self, n):
        self.n = n

    def __next__(self):
        return self.n
    
    def __iter__(self):
        return self