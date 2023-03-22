
#Name: Goutham Selvakumar
#Date: 01/19/2022
#Link: "https://www.loom.com/share/b4a7b8ce64b541bda0feaa942ec2dac3"
#"I have given or recieved any unauthorized assistance on this assignment"

dictionary = {}
"To store the stem and leaf values"

def readFile(filename, dictionary):
    'Reads the file, opens, reads, and then it appends to the dictionary as stem or leaf'
    infile = open(filename, "r")
    lineList = infile.read().split()
    dictionary.clear()
    for num in lineList:
        stem = int(num[0])
        leaf = int(num[1:4])
        if stem in dictionary:
            dictionary[stem].append(leaf)
        else:
            dictionary[stem] = [leaf]

def read_file3(filename, dictionary):     #created for file 3 has it contains 4 digit values
    infile = open(filename, "r")
    lineList = infile.read().split()
    dictionary.clear()
    for num in lineList:
        stem = int(num[0:2])
        leaf = int(num[:5])
        if stem in dictionary:
            dictionary[stem].append(leaf)
        else:
            dictionary[stem] = [leaf]

def StemAndLeaf():
    'Will the show the stem and leaf plot in ascending order'
    print("Stem and leaf plot:\n")
    for first,second in sorted(dictionary.items()):
        line = "|"                      #stem and leaf values are distinguished by creating this variable
        for numbers in sorted(second):
            line = line + " " + str(numbers)
        print(first, line)
        print()

def main():
    print("Hello, Welcome!")  #invoked before loop so that it won't reoccur again 
    while True:
        user = eval(input("\nPlease input 1 2, 3, or 4:\n1. File 1 \n2. File 2 \n3. File 3\n4. Exit the Program\n\nInput your choice: "))
        if user == 1:
            readFile("StemAndLeaf1.txt", dictionary)
            StemAndLeaf()
        elif user == 2:
            readFile("StemAndLeaf2.txt", dictionary)
            StemAndLeaf()
        elif user == 3:
            read_file3("StemAndLeaf3.txt", dictionary)
        elif user == 4:     #This allows the user to exit the program 
            print("GoodBye!")
            break
        else:
            print("Wrong selection try again")  #When the user exceeds the current input values             
            
            
    
