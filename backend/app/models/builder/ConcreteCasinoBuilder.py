from app.models.builder.CasinoBuilder import CasinoBuilder
from app.models.builder.GameTable import GameTable
from app.models.builder.TokenCounter import TokenCounter
from app.models.builder.Bar import Bar
from app.dao.GameTableDao import GameTableDao
from app.dao.BarDao import BarDao
from app.dao.TokenCounterDao import TokenCounterDao
from app.dao.CasinoDao import CasinoDao
from app.dao.StaffDao import StaffDao
import uuid

class ConcreteCasinoBuilder(CasinoBuilder):

    def __init__(self):
        self.TableA = []
        self.TableB = []
        self.TableC = []
        self.TableD = []
        self.Bar = []
        self.StaffId = []
        self.TokenCounterId = None
        self.TokenCounterDao = TokenCounterDao()
        self.StaffDao = StaffDao()
        self.GameTableDao = GameTableDao()
        self.BarDao = BarDao()
        self.CasinoDao = CasinoDao()

    def constructGameTableA(self,number,staffid):

        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.GameTableDao.create_gametable("-1", 0.3, "dice", "A")
            else:
                tableId = self.GameTableDao.create_gametable(staffid[i], 0.3, "dice", "A")
                self.StaffDao.update_assignedId(staffid[i], tableId)
                self.StaffId.append(staffid[i])
            self.TableA.append(tableId)

    def constructGameTableB(self,number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.GameTableDao.create_gametable("-1", 0.7, "card", "B")
            else:
                tableId = self.GameTableDao.create_gametable(staffid[i], 0.7, "card", "B")
                self.StaffDao.update_assignedId(staffid[i], tableId)
                self.StaffId.append(staffid[i])
            self.TableB.append(tableId)

    def constructGameTableC(self,number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.GameTableDao.create_gametable("-1", 0.5, "card", "C")
            else:
                tableId = self.GameTableDao.create_gametable(staffid[i], 0.5, "card", "C")
                self.StaffDao.update_assignedId(staffid[i], tableId)
                self.StaffId.append(staffid[i])
            self.TableC.append(tableId)

    def constructGameTableD(self,number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.GameTableDao.create_gametable("-1", 0.5, "dice", "D")
            else:
                tableId = self.GameTableDao.create_gametable(staffid[i], 0.5, "dice", "D")
                self.StaffDao.update_assignedId(staffid[i], tableId)
                self.StaffId.append(staffid[i])
            self.TableD.append(tableId)

    def constructBar(self, number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                barId = self.BarDao.create_bar("-1", 5)
            else:
                barId = self.BarDao.create_bar(staffid[i], 5)
                self.StaffDao.update_assignedId(staffid[i], barId)
                self.StaffId.append(staffid[i])
            self.Bar.append(barId)

    def constructTokenCounter(self):
        # self.TokenCounterId = self.TokenCounterDao.create_tokencounter()
        self.TokenCounterId = "tokencounter_" + str(uuid.uuid4())
        
    def getResult(self, managerId, casinoType):
        TablesList = self.TableA + self.TableB + self.TableC + self.TableD
        casino_id = "casino" + casinoType + "_" + str(uuid.uuid4())
        self.CasinoDao.add_casinoTokenMg(casino_id, self.TokenCounterId, managerId, casinoType)
        for gameTableid in TablesList:
            self.CasinoDao.add_casinogametable(casino_id, gameTableid)
        for barId in self.Bar:
            self.CasinoDao.add_casinobar(casino_id, barId)

        return casino_id




