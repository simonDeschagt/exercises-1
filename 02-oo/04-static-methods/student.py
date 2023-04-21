class Duration:
    def __init__(self, *, tijd):
        self.__tijd = tijd

    @staticmethod
    def from_hours(amount):
        return Duration(tijd = amount * 3600)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(tijd = amount*60)
    
    @staticmethod
    def from_seconds(amount):
        return Duration(tijd = amount)
    
    @property
    def hours(self):
        return self.__tijd / 3600

    @property
    def minutes(self):
        return self.__tijd /60 
    
    @property
    def seconds(self):
        return self.__tijd