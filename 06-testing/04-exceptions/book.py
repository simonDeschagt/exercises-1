class Book():
    def __init__(self, title, isbn):
        if not Book.__is_valid_title(title):
            raise RuntimeError
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    @staticmethod
    def __is_valid_title(title):
        if (len(title) == 0):
            return False
        return True
    
    @staticmethod
    def __is_valid_isbn(isbn):
        isbn = isbn.replace("-", "")
        isbn = isbn.replace(" ", "")
        if (len(isbn)  != 13):
            return False
        digits = list()
        for x in isbn:
            if (len(digits)%2 != 0):
                digits.append(3*int(x))
            else:
                digits.append(int(x))
        if (sum(digits)%10 != 0):
            return False
        return True