class Car :
    def __init__(self, id, name, make, body, year, value):
        self.__id = id
        self.__name = name
        self.__make = make
        self.__body = body
        self.__year = year
        self.__value = value

    # getters
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_make(self):
        return self.__make
    def get_body(self):
        return self.__body
    def get_year(self):
        return self.__year
    def get_value(self):
        return self.__value

    # Setters
    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_make(self, make):
        self.__make = make
    def set_body(self, body):
        self.__body = body
    def set_year(self, year):
        self.__year = year
    def set_value(self, value):
        self.__value = value


    def __str__(self):
        return f"{self.__id} {self.__name} {self.__make} {self.__body} {self.__year} {self.__value}\n"