
def printFile():
    for i in file:
        print(i)


def create(x):
    #newRow = dict.fromkeys(range(0,10), False)
    
    #matrix = dict.fromkeys(range(x+1), (dict.fromkeys(range(x), False)))
    matrix = [[False]*(x+1) for n in range(x+1)]
    return matrix


def turnOnOrOff(coordsFromX, coordsToX, coordsFromY, coordsToY, x):
    
    for i in range(coordsFromX, coordsToX+1):
    
        for j in range(coordsFromY, coordsToY+1):
        
        
            if x[i][j] == False:
                x[i][j] = True
                
def check(x, L):
    count = 0
    for i in range(0,L):
        for j in range(0,L):
                if x[i][j] and x[i+1][j+1] and x[i][j+1] and x[i+1][j]:
                    x[i][j] = False
                    count+=1
                    
    return count 


    
                
                
                
                
                

# -*- coding: utf-8 -*-




"""Main module."""
