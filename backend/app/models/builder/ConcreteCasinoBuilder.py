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
        self.__TableA = []
        self.__TableB = []
        self.__TableC = []
        self.__TableD = []
        self.__Bar = []
        self.__StaffId = []
        self.__TokenCounterId = None
        self.__TokenCounterDao = TokenCounterDao()
        self.__StaffDao = StaffDao()
        self.__GameTableDao = GameTableDao()
        self.__BarDao = BarDao()
        self.__CasinoDao = CasinoDao()

    def constructGameTableA(self,number,staffid):

        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.__GameTableDao.create_gametable("-1", 0.3, "dice", "A")
            else:
                tableId = self.__GameTableDao.create_gametable(staffid[i], 0.3, "dice", "A")
                self.__StaffDao.update_assignedId(staffid[i], tableId)
                self.__StaffId.append(staffid[i])
            self.__TableA.append(tableId)

    def constructGameTableB(self,number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.__GameTableDao.create_gametable("-1", 0.7, "card", "B")
            else:
                tableId = self.__GameTableDao.create_gametable(staffid[i], 0.7, "card", "B")
                self.__StaffDao.update_assignedId(staffid[i], tableId)
                self.__StaffId.append(staffid[i])
            self.__TableB.append(tableId)

    def constructGameTableC(self,number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.__GameTableDao.create_gametable("-1", 0.5, "card", "C")
            else:
                tableId = self.__GameTableDao.create_gametable(staffid[i], 0.5, "card", "C")
                self.__StaffDao.update_assignedId(staffid[i], tableId)
                self.__StaffId.append(staffid[i])
            self.__TableC.append(tableId)

    def constructGameTableD(self,number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                tableId = self.__GameTableDao.create_gametable("-1", 0.5, "dice", "D")
            else:
                tableId = self.__GameTableDao.create_gametable(staffid[i], 0.5, "dice", "D")
                self.__StaffDao.update_assignedId(staffid[i], tableId)
                self.__StaffId.append(staffid[i])
            self.__TableD.append(tableId)

    def constructBar(self, number,staffid):
        for i in range(number):
            if(i >= len(staffid)):
                barId = self.__BarDao.create_bar("-1", 5)
            else:
                barId = self.__BarDao.create_bar(staffid[i], 5)
                self.__StaffDao.update_assignedId(staffid[i], barId)
                self.__StaffId.append(staffid[i])
            self.__Bar.append(barId)

    def constructTokenCounter(self):
        # self.__TokenCounterId = self.__TokenCounterDao.create_tokencounter()
        self.__TokenCounterId = "tokencounter_" + str(uuid.uuid4())
        
    def getResult(self, managerId, casinoType):
        TablesList = self.__TableA + self.__TableB + self.__TableC + self.__TableD
        casino_id = "casino" + casinoType + "_" + str(uuid.uuid4())
        casino = self.__CasinoDao.add_casinoTokenMg(casino_id, self.__TokenCounterId, managerId, casinoType)
        for gameTableid in TablesList:
            self.__CasinoDao.add_casinogametable(casino_id, gameTableid)
        for barId in self.__Bar:
            self.__CasinoDao.add_casinobar(casino_id, barId)

        return casino




