class TokenCounter:
    def __init__(self, tokencounterid):
        self.__tokencounterid = tokencounterid

    # getters
    def get_id(self):
        return self.__tokencounterid    

    def serialize(self):
        return {
            'id': self.__tokencounterid,
        }
    