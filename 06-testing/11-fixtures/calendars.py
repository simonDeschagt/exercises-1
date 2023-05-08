from datetime import date

class Calendar():
    # def __init__(self):
    #     self.__date = date.today

    # @property
    # def today(self):
    #     return self.__date
    @property
    def today(self):
        return date.today()

class CalenderStub():
    # def __init__(self, date):
    #     self.date == date

    # @property
    # def today(self):
    #     return self.__date
    def __init__(self, today):
        self.today = today