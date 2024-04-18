class Bar:
    def __init__(self, id, name, location, manager):
        self.__id = id
        self.__name = name
        self.__location = location
        self.__manager = manager
    
    # getters
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def get_manager(self):
        return self.__manager
    

    # setters

    def set_name(self, name):
        self.__name = name
    
    def set_location(self, location):
        self.__location = location

    def set_manager(self, manager):
        self.__manager = manager

    def serialize(self):
        return {
            'name': self.__name,
            'location': self.__location,
            'manager': self.__manager.serialize()
        }
