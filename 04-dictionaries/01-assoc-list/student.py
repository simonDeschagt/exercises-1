class AssocList():
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        index = self.__find_key_index(key)

        if index == -1:
            self.__items.append([key, value])
        else:
            self.__items[index][1] = value
    
    def __getitem__(self, key):
        index = self.__find_key_index(key)
        if index == -1:
            raise KeyError()
        return self.__items[index][1]
    
    def __len__(self):
        return len(self.__items)
    
    def __contains__(self, key):
        return self.__find_key_index(key) != -1
    
    def __find_key_index(self, key):
        for i in range(len(self.__items)):
            k, v = self.__items[i]
            if k == key:
                return i
        return -1
    
    # def keys(self):
    #     small_list = list()
    #     for k in self.__items:
    #         small_list.append(k[0])
    #     return small_list
    
    # def values(self):
    #     return None
    
    @property
    def keys(self):
        return [k for k, _ in self.__items]
    
    @property
    def values(self):
        return [v for _, v in self.__items]

al = AssocList()
al['a'] = 1
al['b'] = 2
al['c'] = 3
print(al.keys)#als je een lijst of dergelijke wilt terugkrijgen is het makkelijker om dit te doen met @property, anders krijg je een methode terug en moet je deze nog gaan omzetten