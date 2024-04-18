class TokenCounter:
    def __init__(self, id):
        self.__id = id

    # getters
    def get_id(self):
        return self.__id    

    def serialize(self):
        return {
            'id': self.__id,
        }
    