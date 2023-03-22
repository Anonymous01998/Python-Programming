#NAME: Goutham Selvakumar
#Date: 02-08-2022
#Link: " https://www.loom.com/share/33b9339342154e5d975e537499cf76a7 "
# "I have not given or recieved any unauthorized assistance on this assignment."

import random

class SixSidedDie:
    '''the sixsideddie is being represented'''
    def __init__(self):
        self.r = 0
    
    def roll(self):
        '''roll implementation for sixsideddie'''
        self.r = random.randrange(1,7)
        return self.r

    def getFaceValue(self):
        '''new number is given when the die is rolled return as a facevalue'''
        return self.r
    
    def __repr__(self):
        return "SixSidedDie({})".format(self.r)

class TenSidedDie(SixSidedDie):
    '''the tensideddie is being representated'''
    def roll(self):
        self.r = random.randrange(1,11)
        return self.r

    def __repr__(self):
        return "TenSidedDie({})".format(self.r)

class TwentySidedDie(SixSidedDie):
    '''the twentysideddie is being represented'''
    def roll(self):
        self.r = random.randrange(1,21)
        return self.r

    def __repr__(self):
        return "TwentySidedDie({})".format(self.r)

class Cup:
    '''class representing the cup class'''


    def __init__(self, sixDieCount = 1, tenDieCount = 1, twentyDieCount = 1):
        '''initialize'''
        #three lists are created for each individual dice
        self.sixList = []
        self.tenList = []
        self.twentyList = []
        for i in range(sixDieCount):
            self.sixList.append(SixSidedDie())
        for i in range(tenDieCount):
            self.tenList.append(TenSidedDie())
        for i in range(twentyDieCount):
           self.twentyList.append(TwentySidedDie())

    def roll(self):
        '''the dices are rolled in the cup'''
        self.r = 0
        for i in self.sixList:
            self.r += i.roll()
        for i in self.tenList:
            self.r += i.roll()
        for i in self.twentyList:
            self.r += i.roll()
        return self.r

    def getSum(self):
        return self.r

    def __repr__(self):
        sixDisStr = ",".join([str(x) for x in self.sixList])
        tenDisStr = ",".join([str(x) for x in self.tenList])
        twentyDisStr = ",".join([str(x) for x in self.twentyList])
        return "Cup({},{},{})".format(sixDisStr, tenDisStr, twentyDisStr)





        
        

  


    
        
