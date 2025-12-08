class Student :
    def __init__(self, id, f_name, l_name, gpa, semester):
        self.__id = id
        self.__f_name = f_name
        self.__l_name = l_name
        self.__gpa = gpa
        self.__semester = semester

    # getters
    def get_id(self) :
        return self.__id
    def get_f_name(self) :
        return self.__f_name
    def get_l_name(self) :
        return self.__l_name
    def get_gpa(self) :
        return self.__gpa
    def get_semester(self) :
        return self.__semester

    # setters
    def set_id(self, id):
        self.__id = id
    def set_f_name(self, f_name):
        self.__f_name = f_name
    def set_l_name(self, l_name):
        self.__l_name = l_name
    def set_id(self, gpa):
        self.__gpa = gpa
    def set_id(self, semester):
        self.__semester = semester
