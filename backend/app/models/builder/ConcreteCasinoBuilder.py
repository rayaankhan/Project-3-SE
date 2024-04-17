from app.models.builder.CasinoBuilder import CasinoBuilder
from app.models.builder.GameTable import GameTable
from app.models.builder.TokenCounter import TokenCounter
from app.models.builder.Bar import Bar
from app.dao.GameTableDao import GameTableDao
from app.dao.BarDao import BarDao
from app.dao.TokenCounterDao import TokenCounterDao
from app.dao.CasinoDao import CasinoDao
import uuid

class ConcreteCasinoBuilder(CasinoBuilder):

    def __init__(self):
        self.TableA = []
        self.TableB = []
        self.TableC = []
        self.TableD = []
        self.Bar = []
        self.StaffId = []
        self.TokenCounter = None
        self.TokenCounterDao = TokenCounterDao()
        self.GameTableDao = GameTableDao()
        self.BarDao = BarDao()
        self.CasinoDao = CasinoDao()

    def constructGameTableA(self,number,staffid):

        for i in range(number):
            self.TableA.append(self.GameTableDao.create_gametable(staffid[i], 0.3, "dice"))
            self.StaffId.append(staffid[i])

    def constructGameTableB(self,number,staffid):
        for i in range(number):
            self.TableB.append(self.GameTableDao.create_gametable(staffid[i], 0.7, "card"))
            self.StaffId.append(staffid[i])

    def constructGameTableC(self,number,staffid):
        for i in range(number):
            self.TableC.append(self.GameTableDao.create_gametable(staffid[i], 0.5, "card"))
            self.StaffId.append(staffid[i])

    def constructGameTableD(self,number,staffid):
        for i in range(number):
            self.TableD.append(self.GameTableDao.create_gametable(staffid[i], 0.5, "dice"))
            self.StaffId.append(staffid[i])

    def constructBar(self, number,staffid):
        for _ in range(number):
            self.Bar.append(self.BarDao.create_bar(staffid, 5))

    def constructTokenCounter(self):
        self.TokenCounter = self.TokenCounterDao.create_tokencounter()
        
    def getResult(self):
        TablesList = self.TableA + self.TableB + self.TableC + self.TableD
        id = str(uuid.uuid4())
        for i in range(TablesList):
            for j in range(self.StaffId):
                for k in range(self.Bar):
                    self.CasinoDao.create_casino(i,j,k,self.TokenCounter, managerid)




