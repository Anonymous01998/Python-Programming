#NAME - GOUTHAM SELVAKUMAR 
#DATE - 03/08/2022
#LINK - "https://www.loom.com/share/3fcf8b69c80149248662970fb25fdb9f"
# "I have not given or recieved any unauthorized assistance on this assignment"


import numpy as np
import matplotlib.pyplot as plt

def display(board,t=0):
    print("Advance Step:",t)
    fig, ax = plt.subplots()                          #makes a figure and an axis of the plot
    img = ax.imshow(board, plt.cm.binary_r)           #shows the conway board
    

def conway(s,p):
    """This function creates a board with live and dead cells. The board is a two-dimensional square board"""
    rs = int(s ** 0.5)                                 #working out the rows and columns utilizing the shape
    board = np.random.rand(rs,rs)                      #producing an arbitary 2D exhibit
    board = (board < p) * 1                            #thresholding utilizing the likely to create the dead and live cells 
    
                                                       #print("Board Initialization")
    display(board)
    return(board)
    
def advance(b,t):
    nrows, ncols = b.shape                             #deriving the number of rows and columns of the board
    
    for i in range(t):                                 #Advances 't' times
                                                       #print("Advance Step",t)
        nextGen = np.zeros((nrows,ncols), dtype=int)   #generate a new board for the next generation
        for row in range(nrows):
            for col in range(ncols):                   
                curr = b[row][col]                     #derives the current cell value
               
                                                       #determines the upsides of the 4-neighbours 
                left = b[row][col-1]
                right = b[row][(col+1)%ncols]
                top = b[row-1][col]
                down = b[(row+1)%nrows][col]
                liveNeighbours = left+right+top+down   #computing the number of dynamic neighbours
                if curr == 0:                          #Logic used to update the board 
                     if liveNeighbours == 3:
                         nextGen[row][col] = 1
                else:
                    if liveNeighbours <2:
                        nextGen[row][col] = 0
                    elif liveNeighbours ==2 or liveNeighbours == 3:
                        nextGen[row][col] = 1
                    elif liveNeighbours > 3:
                        nextGen [row][col] = 0
        b = nextGen                                     #alloting the next generation board to the current board            
        display(b,i+1)        
        
    
if __name__ == '__main__':
    b = conway(200,0.5)
    advance(b,3)
