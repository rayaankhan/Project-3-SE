class User:
    def __init__(self, id, username, email, age, password):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__age = age
        self.__password = password

    # getters
    def get_id(self):
        return self.__id
    
    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age
    
    def get_password(self):
        return self.__password
    
    # setters
    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_age(self, age):
        self.__age = age

    def set_password(self, password):
        self.__password = password

    def serialize(self):
        return {
            'id': self.__id,
            'username': self.__username,
            'email': self.__email,
            'age': self.__age
        }
    

    
