class CircularBuffer:
    def __init__(self, size):
        self.list = list()
        self.size = size

    def add(self, item):
        if len(self.list) < self.size:
            self.list.append(item)
        else:
            self.list.pop(0)
            self.list.append(item)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, value):
        return self.list[value]
    