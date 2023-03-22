#NAME : GOUTHAM SELVAKUMAR
#DATE : 03/17/2022
#LINK : "https://www.loom.com/share/e0bdfa49baec4e7a98d9afe1c9f08b06"
# “I have not given or received any unauthorized assistance on this assignment.” 


import pandas as pd                          #imports pandas
from numpy import random
import numpy as np

ratList = []
catList = []
berriesBasket = []

def readFile():                              #reads the specified parameter txt
    """This function is reading the parameters in a parameter document and storing them in a list"""

    parameters = {}

    with open("parameters.txt") as file:

        for parameter in file.readlines():
            parameter = parameter.strip('\n').split('=')
            parameters[parameter[0]] = parameter[1]

        return list(parameters.values())

def rain():
    '''This function determines whether it will rain'''
    
    if random.rand() < float(readFile()[1]) :
        return 0
       
    return random.normal(float(readFile()[2]),float(readFile()[4]), size=(1, 1))[0][0]
    
def generateRat():
    """This function initializes the rats in the island"""
    
    num_rat=int(readFile()[6])
    for i in range(num_rat):
        rat = Rats(random.randint(0, num_rat))
        ratList.append(rat)

def generateCat():
    """This function initializes the cat in the island"""
    
    num_cat = int(readFile()[14])
    for _ in range(0, num_cat):
        cat = Cats(random.randint(0, num_cat))
        catList.append(cat)

def deleteDeadObject():
    """This function removes the cat or rat in case it is dead. Need to eliminate them all"""
    
    for berry in berriesBasket:                     
        if not berry.isEatable():
            berriesBasket.remove(berry)
    for rat in ratList:
        if rat.isDead():
            ratList.remove(rat)
    for cat in catList:
        if cat.isDead():
            catList.remove(cat)


class Rats :
    '''This class represents a rat that inherits from an Island'''

    def __init__(self, age):
        
        #define the constructor variables
        self.ratsBirth_initBerries = int(readFile()[5])
        self.numRats = int(readFile()[6])
        self.ratCoeff = int(readFile()[7])
        self.ratDays = int(readFile()[8])
        self.ratRange = int(readFile()[9])
        self.ratTotalBerries = int(readFile()[10])
        self.berryAfter = int(readFile()[11])
        self.uniformDistStart = int(readFile()[12])
        self.uniformDistEnd = int(readFile()[13])
        self.ratsBeginAge = int(readFile()[19])
        self.days = age
        self.eatDaysAgo = 0
        self.berriesEaten = 0

    def passDay(self):
        self.days += 1
        self.eatDaysAgo += 1
        
            
    def tryEat(self):
        """This is a function to run eating berries"""

        berriesNum = len(berriesBasket)
        if berriesNum > 0:
            r = random.randint(0, berriesNum)
            self.eatDaysAgo = 0
            self.berriesEaten += 1
            del berriesBasket[r]
    
    def isDead(self):
        """This is the function that simulate rats dead"""
        
        if self.eatDaysAgo >= 3:
            return True
        if self.days > self.ratTotalBerries and (random.rand() < 0.01 * 0.05 * (self.days - 49)):
            return True
        return False
    
               
    def givingBirth(self):
        """This is the function to simulate rat birth"""
        
        if self.berriesEaten < self.ratsBirth_initBerries:
            return
        if (self.berriesEaten - self.ratsBirth_initBerries) % self.berryAfter == 0:
            ratsBorn = random.randint(self.uniformDistStart, self.uniformDistEnd + 1)
            for r in range(1, ratsBorn):
                ratList.append(Rats(0))

class Cats:
    '''This is the class that represents a cat'''

    def __init__(self, age):
        
        self.islandArea = int(readFile()[0])
        self.numCats = int(readFile()[14])
        self.maxCatAge = int(readFile()[15])
        self.catchProb = float(readFile()[16])
        self.expProb = float(readFile()[17])
        self.catDaysDie = int(readFile()[18])
        self.catRatEat = int(readFile()[19])
        self.catAdditional = int(readFile()[20])
        self.litterSizeStart = int(readFile()[21])
        self.litterSizeEnd = int(readFile()[22])
        self.days = age
        self.eatDaysAgo = 0
        self.ratsEaten = 0

    def passDay(self):
        self.days += 1
        self.eatDaysAgo += 1

    def tryEat(self):
        """This function simulates eat rats"""
        ratsNum = len(ratList)
        if ratsNum > 0 and(random.rand() < (self.catchProb * ratsNum) / self.islandArea + self.days * 5):
            r = random.randint(0, ratsNum)
            self.eatDaysAgo = 0
            self.ratsEaten += 1
            del ratList[r]

    def isDead(self):
        """This function simulate Cat is dead"""
        if self.eatDaysAgo >= 5: # no eat in 5 days.
            return True
        if self.days > self.catDaysDie and (random.rand() < 0.01 * (self.expProb + self.catchProb * (self.days - self.catDaysDie))):
                return True
        return False

    def givingBirth(self):
        """This function simulate cat birth"""
        if self.ratsEaten < self.catRatEat: 
            return
        if (self.ratsEaten - self.catRatEat) % self.catAdditional == 0:
            rats_born = random.randint(self.litterSizeEnd, self.litterSizeStart + 1)
            for k in range(0, rats_born):
                catList.append(Cats(0))
                

class Berry:
    def __init__(self):
        self.ageDays = 0
        self.berryPersist = int(readFile()[5])

    def isEatable(self):
        return self.ageDays <= self.berryPersist

    def passDay(self):
        self.ageDays += 1

def simulation():
    """This function performs simulation of the assignment"""
    rainn = int(0)
    generateRat()
    generateCat()
    daysLimit = 2
    islandArea = int(readFile()[0])
    berryCoeff = float(readFile()[3])
    for i in range(1, daysLimit):
        newBerries = int(rainn * islandArea * berryCoeff) 
        for berry in range(1, newBerries):
            berriesBasket.append(Berry())
        for berry in berriesBasket:
            berry.passDay()
        for rat in ratList:
            rat.tryEat()
            rat.givingBirth()
            rat.passDay()
        for cat in catList:
            cat.tryEat()
            cat.givingBirth()
            cat.passDay()
        rainn = rain()
        deleteDeadObject()

def main():
    simulation()
    daysLimit = 10
    print("Simulator in {} days".format(str(daysLimit)))
    print("Berries population: {} ea".format(str(len(berriesBasket))))
    print("Rats population: {} ea".format(str(len(ratList))))
    print("Cats population: {} ea".format(str(len(catList))))
    out = open("output.txt", "w")
    out.write("Simulator in " + str(daysLimit) + "days\n")
    out.write("Berries population: "+ "\n")
    out.write("Rats population: " + "\n")
    out.write("Cats population: " + "\n")
    out.close()

main()
