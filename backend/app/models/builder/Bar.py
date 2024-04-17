class Bar:
    def __init__(self, id, staffid, drinks):
        self.__id = id
        self.__staffid = staffid
        self.__drinks = drinks

    # getters
    def get_id(self):
        return self.__id

    def get_staffid(self):
        return self.__staffid

    def get_drinks(self):
        return self.__drinks
    

    def serialize(self):
        return {
            'id': self.__id,
            'staffid': self.__username
        }
    