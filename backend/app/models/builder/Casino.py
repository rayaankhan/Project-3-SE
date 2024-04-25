from app.models.Observer import Subject
from app.dao.SubscriptionDao import SubscriptionDao
from app.dao.UserDao import UserDao
from app.models.User import User

user_dao = UserDao()
class Casino(Subject):
    def __init__(self, casinoid, casinoname, tokencountername, tokencounterid, managerid):
        self.__casinoid = casinoid
        self.__casinoname = casinoname
        self.__tokencountername = tokencountername
        self.__tokencounterid = tokencounterid
        self.__managerid = managerid

    # getters
    def get_casinoid(self):
        return self.__casinoid
    
    def get_casinoname(self):
        return self.__casinoname
    
    def get_tokencountername(self):
        return self.__tokencountername
    
    def get_tokencounterid(self):
        return self.__tokencounterid
    
    def get_managerid(self):
        return self.__managerid

    def serialize(self):
        return {
            'id': self.__casinoid,
            'casinoname': self.__casinoname
        }
    
    def check_subscription(self, userId):
        return SubscriptionDao.check_user_subscription(userId, self.__casinoid)

    def attach(self, userId):
        userid = SubscriptionDao.create_user_subscription(userId, self.__casinoid)
        if(userid):
            print(f"User {userId} subscribed to casino {self.__casinoid}")

    def detach(self, userId):
        userid = SubscriptionDao.remove_user_subscription(userId, self.__casinoid)
        if(userid):
            print(f"User {userId} unsubscribed from casino {self.__casinoid}")

    def notify(self, message):
        subscriptionIds = SubscriptionDao.get_subscribers_by_casino_id(self.__casinoid)
        for subscriptionId in subscriptionIds:
            print(f"Sending notification to user {subscriptionId}")
            user = user_dao.get_user_by_id(subscriptionId)
            if(type(user) is User):
                user.update(message, self.__casinoid)
                user_dao.add_notification_to_db(subscriptionId, message, self.__casinoid)

    def send_notification(self, message):
        print(f"Casino {self.__casinoid} is sending notification: {message}")
        self.notify(message)
    

    
