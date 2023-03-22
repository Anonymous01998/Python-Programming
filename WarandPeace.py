#NAME - Goutham Selvakumar
#DATE - 02/22/2022
#LINK - "https://www.loom.com/share/2d4fb3e400324d19a0eaf7fcbfa3984a"
# "I have not given or recieved any unauthorized assistance on this assignment."

import numpy as np

class WarAndPeacePseudoRandomNumberGenerator():
    '''This class uses the text file war-and-peace.txt to generate psuedo random numbers'''

    def __init__(self, get_seed=12345):
        self.seed = get_seed                                                                                        

    def binary_vals(self):
        file = open('war-and-peace.txt', 'r')   #text file opening
        line = file.read(self.seed)             #number of bits are initialized
        a = line[self.seed - 1]                                                                                     
        b = line[self.seed - 100]                                       
        if a > b:
            return True
        elif a < b:
            return False
        else:
            while a == b:
                a = line[self.seed - 1]                                                         
                b = line[self.seed - 3]
                self.seed = self.seed - 1
            if a > b:
                return True
            elif a < b:
                return False

    def random_vals(self):
        '''this function generates 0 and 1 for 32 bits'''
        randomNumbers = []
        for x in range(1, 1001):  #list of random numbers generated from 0 and 1000
            lst = []
            lst2 = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.007813, 0.003906, 0.001953]
            lst3 = []
            rnd = 0

            for i in range(1, 9):
                x = WarAndPeacePseudoRandomNumberGenerator.binary_vals(self)
                if x == True:
                    lst.append(1)                                                                                   
                else:
                    lst.append(0)                                           
                self.seed = self.seed + 1                                                                               

            for j in range(0, len(lst)):
                lst3.append((lst[j] * lst2[j]))

            for k in range(0, len(lst3)):
                rnd = rnd + lst3[k]         
            randomNumbers.append(rnd)   #appending the numbers 
            self.seed += 1


        print("Mean of the pseudo random numbers:", np.mean(randomNumbers))
        print("Minimum number:",np.min(randomNumbers))
        print("Maximum number:",np.max(randomNumbers))


prng = WarAndPeacePseudoRandomNumberGenerator(12345)
prng.random_vals()




