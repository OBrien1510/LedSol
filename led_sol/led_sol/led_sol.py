def create(x):
    #newRow = dict.fromkeys(range(0,10), False)
    
    #matrix = dict.fromkeys(range(x+1), (dict.fromkeys(range(x), False)))
    
    matrix = [[False]*(x+1) for n in range(x+1)]
    
    return matrix



def turnOnOrOf():
    
    newMatrix = create(L)
    
    for i in range(coordsFromX, coordsToX+1):
    
        for j in range(coordsFromY, coordsToY+1):
        
        
            if newMatrix[i][j] == False:
                newMatrix[i][j] = True
# -*- coding: utf-8 -*-

"""Main module."""
