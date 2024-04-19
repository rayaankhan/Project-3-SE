import random

class GameTable:
    def __init__(self, gametableid, name, staffid, prob, type):
        self.__gametableid = gametableid
        self.__name = name
        self.__staffid = staffid
        self.__prob = prob
        self.__type = type

    # getters
    def get_id(self):
        return self.__gametableid
    
    def get_name(self):
        return self.__name

    def get_staffid(self):
        return self.__staffid

    def get_prob(self):
        return self.__prob
    
    def get_type(self):
        return self.__type
    
    def generate_random_number_with_probability(self, max_cap, user_amount):
        # Generate a random number between 0 and 1000
        random_number = random.randint(0, max_cap)

        # Generate a random probability between 0 and 1
        probability = random.random()

        # Check if the random number is more than the particular amount based on probability
        if probability <= self.__prob and random_number <= user_amount:
            # If the random number is less than or equal to the particular amount, generate a new number
            return self.generate_random_number_with_probability(max_cap, user_amount)
        else:
            return random_number
    
    def play(self, user_amount):
        multiplier = 2
        final_amount = self.generate_random_number_with_probability(multiplier*user_amount, user_amount)
        return final_amount
    

    def serialize(self):
        return {
            'id': self.__gametableid,
            'staffid': self.__staffid
        }
    