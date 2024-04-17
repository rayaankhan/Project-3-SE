from CasinoBuilder import CasinoBuilder

class CasinoDirector:
    
    def constructCasinoA(casinobuilder,number1,number2,number3,staffid):
        staffid1 = []
        staffid2 = []
        staffid3 = None
        for i in range(len(staffid)):
            if(i<number1):
                staffid1.append(staffid[i])
            elif(i!=(len(staffid)-1)):
                staffid2.append(staffid[i])
            else:
                staffid3 = staffid[i]
        casinobuilder.constructGameTableA(number1,staffid1)
        casinobuilder.constructGameTableC(number2,staffid2)
        casinobuilder.constructTokenCounter()
        casinobuilder.constructBar(number3,staffid3)

    def constructCasinoB(casinobuilder,number1,number2,number3,staffid):
        staffid1 = []
        staffid2 = []
        staffid3 = None
        for i in range(len(staffid)):
            if(i<number1):
                staffid1.append(staffid[i])
            elif(i!=(len(staffid)-1)):
                staffid2.append(staffid[i])
            else:
                staffid3 = staffid[i]
        casinobuilder.constructGameTableA(number1,staffid1)
        casinobuilder.constructGameTableB(number2,staffid2)
        casinobuilder.constructTokenCounter()
        casinobuilder.constructBar(number3,staffid3)

    def constructCasinoC(casinobuilder,number1,number2,number3,staffid):
        staffid1 = []
        staffid2 = []
        staffid3 = None
        for i in range(len(staffid)):
            if(i<number1):
                staffid1.append(staffid[i])
            elif(i!=(len(staffid)-1)):
                staffid2.append(staffid[i])
            else:
                staffid3 = staffid[i]
        casinobuilder.constructGameTableC(number1,staffid1)
        casinobuilder.constructGameTableD(number2,staffid2)
        casinobuilder.constructTokenCounter()
        casinobuilder.constructBar(number3,staffid3)

    def constructCasinoD(casinobuilder,number1,number2,number3,staffid):
        staffid1 = []
        staffid2 = []
        staffid3 = None
        for i in range(len(staffid)):
            if(i<number1):
                staffid1.append(staffid[i])
            elif(i!=(len(staffid)-1)):
                staffid2.append(staffid[i])
            else:
                staffid3 = staffid[i]
        casinobuilder.constructGameTableB(number1,staffid1)
        casinobuilder.constructGameTableD(number2,staffid2)
        casinobuilder.constructTokenCounter()
        casinobuilder.constructBar(number3,staffid3)



