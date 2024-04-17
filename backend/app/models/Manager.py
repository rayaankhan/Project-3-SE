class Manager:
    # casinos is a list of Casino objects by default it is an empty list
    def __init__(self, id, salary, casinos=[]):
        self.__id = id
        self.__salary = salary
        self.__casinos = casinos

    # getters
    def get_id(self):
        return self.__id
    
    def get_salary(self):
        return self.__salary
    
    def get_casinos(self):
        return self.__casinos
    
    # setters
    def set_salary(self, salary):
        self.__salary = salary

    def set_casinos(self, casinos):
        self.__casinos = casinos

    def serialize(self):
        return {
            'salary': self.__salary,
            'casinos': [casino.serialize() for casino in self.__casinos]
        }

    

    
