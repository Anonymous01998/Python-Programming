#NAME - Goutham Selvakumar
#DATE - 03/02/2022
#LINK - "https://www.loom.com/share/d5091000dd784e579e77f8d94e1c17fe"
# "I have not given or recieved any unauthorized assistance on this assisgnment."

import random

class SimplePlotGenerator:    
    """
    simple plot generator class which goes about as a fundamental class for other plot classes to extend
    """
    
    def __init__(self):
        self.view = self
    
    def registerView(self,view):
        self.view = view
        
    def generate(self):
        return "Something Happens"
    
class RandomPlotGenerator(SimplePlotGenerator):    
    """
    random plot generator class extending simplePlotGenerator and superseding the general method just returning a plot
    """
    
    def generate(self):
        '''returns a plot string with various irregular plot strings'''
        #fileNames contains the name of all the textfiles
        fileNames = ['plot_names.txt','plot_adjectives.txt', 'plot_profesions.txt', 'plot_verbs.txt', 'plot_adjectives_evil.txt', 'plot_villian_job.txt', 'plot_villains.txt', ]
        
        #word is utilized to gather the irregular words from the text document to produce a plot
        word = []
        
        #loops through every text document and picks an irregular word to produce the plot
        for i in range(len(fileNames)):
            f = open(fileNames[i], 'r')
            content = f.readlines()
            #chooses random word and strips whitespaces
            word.append(random.choice(content).strip())
            f.close()
        
        #makes the plot utilizing randomly picked words from various text documents
        self.sequence = "{}, a {}, must {} the {} {}, {}.".format(word[0],word[1],word[2],word[3],word[4],word[5],word[6])
        return self.sequence 

class InteractivePlotGenerator (SimplePlotGenerator):    
    """
    Interactive plot generator class extending the simpleplotgenerator and superseding the generate method just returning a plot connecting with the view
    """
        
    def queryUser(self):
        '''This function accepts the choices from the user and generates a plot of their choice'''
        
        if self.view == self:
            print("*********I am in local machine. I'm not connected to any view*********\n")
            fileNames = ['plot_names.txt','plot_adjectives.txt', 'plot_profesions.txt', 'plot_verbs.txt', 'plot_adjectives_evil.txt', 'plot_villian_job.txt', 'plot_villains.txt', ]
            #stores the words to generate a plot
            word = [] 
            for i in range(len(fileNames)): ##loops through all the files
                selection =[]
                f = open(fileNames[i], 'r')
                content = f.readlines()
                f.close()
                for j in range(5):
                    #randomly picks words from the text file
                    selection.append(random.choice(content).strip())
                
                while True:
                    #queries the user for their choice
                    print("{}".format(selection),end = "")
                    choice = int(input("Enter a number index for 0,1,2,3,4....."))
                    if(choice<=4 and choice>=0):
                        word.append(selection[choice])
                        break
                    else:
                        print("The user input is invalid. If it is not too much trouble, attempt again a numeric number between 0-4 as it were")
                        
            #creates the plot using user picked words from different text files
            self.sequence = "{0}, a {1} {2}, must {3} the {4} {5}, {6}.".format(word[0],word[1],word[2],word[3],word[4],word[5],word[6])
        
        else:
            #uses the interface of the plot viewer if the view is registered with the generator
            self.sequence = self.view.queryUser()
        return self.sequence
        
    def generate(self):
        return(self.queryUser())
        
        
        
def main():
    print("SimplePlotGenerator")
    a = SimplePlotGenerator()
    print(a.generate())
    print("RandomPlotGenerator")
    b = RandomPlotGenerator()
    print(b.generate())
    print("InteractivePlotGenerator")
    c = InteractivePlotGenerator()
    print(c.generate())


if __name__ == "__main__":
    main()
