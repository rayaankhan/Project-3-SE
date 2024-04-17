class GameTable:
    def __init__(self, id, staffid, prob, type):
        self.__id = id
        self.__staffid = staffid
        self.__prob = prob
        self.__type = type

    # getters
    def get_id(self):
        return self.__id

    def get_staffid(self):
        return self.__staffid

    def get_prob(self):
        return self.__prob
    
    def get_type(self):
        return self.__type
    

    def serialize(self):
        return {
            'id': self.__id,
            'staffid': self.__username
        }
    