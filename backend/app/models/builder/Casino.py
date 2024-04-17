class Casino:
    def __init__(self, id, gametableid, barid, tokencounterid, managerid):
        self.__id = id
        self.__gametableid = gametableid
        self.__barid = barid
        self.__tokencounterid = tokencounterid
        self.__managerid = managerid

    # getters
    def get_id(self):
        return self.__id
    
    def get_barid(self):
        return self.__barid
    
    def get_gametableid(self):
        return self.__gametableid

    def get_tokencounterid(self):
        return self.__tokencounterid
    
    def get_managerid(self):
        return self.__managerid
    
    # # setters
    # def set_username(self, username):
    #     self.__username = username

    # def set_email(self, email):
    #     self.__email = email

    # def set_age(self, age):
    #     self.__age = age

    # def set_password(self, password):
    #     self.__password = password

    def serialize(self):
        return {
            'id': self.__id,
            'gametable': self.__gametableid,
            'bar': self.__barid,
            'tokencounter': self.__tokencounterid,
            'manager': self.__managerid
        }
    

    
