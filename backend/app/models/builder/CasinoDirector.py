
class CasinoDirector:

    def __init__(self, builder, tableA, tableB, tableC, tableD, num_bar, stafflist, casinoType):
        self.__casinobuilder = builder
        self.__tableA = tableA
        self.__tableB = tableB
        self.__tableC = tableC
        self.__tableD = tableD
        self.__num_bar = num_bar
        self.__staffid = stafflist
        self.__casinoType = casinoType
    
    def constructCasinoA(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.__staffid)):
            if(i < self.__tableA):
                staffid1.append(self.__staffid[i])
            elif(i >= self.__tableA and i < self.__tableA+self.__tableC):
                staffid2.append(self.__staffid[i])
            else:
                staffid3.append(self.__staffid[i])
        self.__casinobuilder.constructGameTableA(self.__tableA,staffid1)
        self.__casinobuilder.constructGameTableC(self.__tableC,staffid2)
        self.__casinobuilder.constructTokenCounter()
        self.__casinobuilder.constructBar(self.__num_bar,staffid3)

    def constructCasinoB(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.__staffid)):
            if(i<self.__tableA):
                staffid1.append(self.__staffid[i])
            elif(i >= self.__tableA and i < self.__tableA+self.__tableB):
                staffid2.append(self.__staffid[i])
            else:
                staffid3.append(self.__staffid[i])
        self.__casinobuilder.constructGameTableA(self.__tableA,staffid1)
        self.__casinobuilder.constructGameTableB(self.__tableB,staffid2)
        self.__casinobuilder.constructTokenCounter()
        self.__casinobuilder.constructBar(self.__num_bar,staffid3)

    def constructCasinoC(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.__staffid)):
            if(i<self.__tableC):
                staffid1.append(self.__staffid[i])
            elif(i >= self.__tableC and i < self.__tableC+self.__tableD):
                staffid2.append(self.__staffid[i])
            else:
                staffid3.append(self.__staffid[i])
        self.__casinobuilder.constructGameTableC(self.__tableC,staffid1)
        self.__casinobuilder.constructGameTableD(self.__tableD,staffid2)
        self.__casinobuilder.constructTokenCounter()
        self.__casinobuilder.constructBar(self.__num_bar,staffid3)

    def constructCasinoD(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.__staffid)):
            if(i<self.__tableB):
                staffid1.append(self.__staffid[i])
            elif(i >= self.__tableB and i < self.__tableB+self.__tableD):
                staffid2.append(self.__staffid[i])
            else:
                staffid3.append(self.__staffid[i])
        self.__casinobuilder.constructGameTableB(self.__tableB,staffid1)
        self.__casinobuilder.constructGameTableD(self.__tableD,staffid2)
        self.__casinobuilder.constructTokenCounter()
        self.__casinobuilder.constructBar(self.__num_bar,staffid3)



