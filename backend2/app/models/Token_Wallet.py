class Token_Wallet():
    def __init__(self, walletid, userid):
        self.__walletid = walletid
        self.__userid = userid

    def get_walletid(self):
        return self.__walletid
    
    def get_userid(self):
        return self.__userid
    
    def serialize(self):
        return {
            'walletid': self.__walletid,
            'userid': self.__userid
        }