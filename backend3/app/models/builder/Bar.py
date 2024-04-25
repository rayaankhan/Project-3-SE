class Bar:
    def __init__(self, barid, name, staffid, drinks):
        self.__barid = barid
        self.__name = name
        self.__staffid = staffid
        self.__drinks = drinks

    # getters
    def get_id(self):
        return self.__barid
    
    def get_name(self):
        return self.__name

    def get_staffid(self):
        return self.__staffid

    def get_drinks(self):
        return self.__drinks
    
    def get_order(self):
        return "Taking the order for drinks"
    
    def giving_order(self):
        return "Giving the drinks"
    

    def serialize(self):
        return {
            'id': self.__barid,
            'staffid': self.__staffid
        }
    