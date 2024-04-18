
class CasinoDirector:

    def __init__(self, builder, tableA, tableB, tableC, tableD, num_bar, stafflist, casinoType):
        self.casinobuilder = builder
        self.tableA = tableA
        self.tableB = tableB
        self.tableC = tableC
        self.tableD = tableD
        self.num_bar = num_bar
        self.staffid = stafflist
        self.casinoType = casinoType
    
    def constructCasinoA(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.staffid)):
            if(i < self.tableA):
                staffid1.append(self.staffid[i])
            elif(i >= self.tableA and i < self.tableA+self.tableC):
                staffid2.append(self.staffid[i])
            else:
                staffid3.append(self.staffid[i])
        self.casinobuilder.constructGameTableA(self.tableA,staffid1)
        self.casinobuilder.constructGameTableC(self.tableC,staffid2)
        self.casinobuilder.constructTokenCounter()
        self.casinobuilder.constructBar(self.num_bar,staffid3)

    def constructCasinoB(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.staffid)):
            if(i<self.tableA):
                staffid1.append(self.staffid[i])
            elif(i >= self.tableA and i < self.tableA+self.tableB):
                staffid2.append(self.staffid[i])
            else:
                staffid3.append(self.staffid[i])
        self.casinobuilder.constructGameTableA(self.tableA,staffid1)
        self.casinobuilder.constructGameTableB(self.tableB,staffid2)
        self.casinobuilder.constructTokenCounter()
        self.casinobuilder.constructBar(self.num_bar,staffid3)

    def constructCasinoC(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.staffid)):
            if(i<self.tableC):
                staffid1.append(self.staffid[i])
            elif(i >= self.tableC and i < self.tableC+self.tableD):
                staffid2.append(self.staffid[i])
            else:
                staffid3.append(self.staffid[i])
        self.casinobuilder.constructGameTableC(self.tableC,staffid1)
        self.casinobuilder.constructGameTableD(self.tableD,staffid2)
        self.casinobuilder.constructTokenCounter()
        self.casinobuilder.constructBar(self.num_bar,staffid3)

    def constructCasinoD(self):
        staffid1 = []
        staffid2 = []
        staffid3 = []
        for i in range(len(self.staffid)):
            if(i<self.tableB):
                staffid1.append(self.staffid[i])
            elif(i >= self.tableB and i < self.tableB+self.tableD):
                staffid2.append(self.staffid[i])
            else:
                staffid3.append(self.staffid[i])
        self.casinobuilder.constructGameTableB(self.tableB,staffid1)
        self.casinobuilder.constructGameTableD(self.tableD,staffid2)
        self.casinobuilder.constructTokenCounter()
        self.casinobuilder.constructBar(self.num_bar,staffid3)



