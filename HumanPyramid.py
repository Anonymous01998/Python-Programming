#NAME :Goutham Selvakumar
#DATE :02/01/2022
#LINK :" https://www.loom.com/share/72e2fc0508c649dfb4c638c98fd49475 "
# "I have not given or recieved any unauthorized assistance on this asssignment."

def getRandC():
    '''Get the row and column'''
    inputs = input("Please enter numbers for row and column: ")
    if inputs=='':
        return '',''
    row,column = eval(inputs)
    return row,column

def humanPyramid(row, column):
    if row == 0:
        weight = 0
        return weight
    else:
        if column == 0:
            weight = (128+humanPyramid(row-1, column))/2
        elif row == column:
            weight = (128+humanPyramid(row-1, column -1))/2
        else:
            weight = (128+humanPyramid(row -1, column))/2 + (128+humanPyramid(row-1, column-1))//2
        return weight    
            
def print_weight(weight):
    '''Print the weights'''
    print(weight)

def main():
    while True:
        r,c = getRandC()
        if r=='':
            print('Exit the Program')
            break
        w = humanPyramid(r, c)
        print_weight(w)
        
'''Defining the main fucntion'''
main()



                
    
    
