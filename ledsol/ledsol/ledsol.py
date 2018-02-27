from ledread import ledread


def main():
    matrix = ledread.firstLine()
    finalMatrix = ledread.read(matrix)
    count = check(finalMatrix)
    print("number of lights on at end of sequence: ",count)

def create(x):
    #newRow = dict.fromkeys(range(0,10), False)
    
    #matrix = dict.fromkeys(range(x+1), (dict.fromkeys(range(x), False)))
    matrix = [[False]*(x+1) for n in range(x+1)]
    return matrix


def turnOnOrOff(coordsFromX, coordsToX, coordsFromY, coordsToY, x, cmd):
    
    for i in range(coordsFromX, coordsToX+1):
    
        for j in range(coordsFromY, coordsToY+1):
        
        
            if x[i][j] == False and (cmd == "turnon" or cmd == "switch"):
                x[i][j] = True
            
            elif x[i][j] == True and (cmd == "turnoff" or cmd == "switch"):
                x[i][j] = False
                
    return x
                
def check(x):
    count = 0
    for i in range(0,len(x)):
        
        for j in range(1, len(x[0])):
            
            if x[i][j] == True:
                
                count+=1
                    
    return count 


    
                
                
                
                
                

# -*- coding: utf-8 -*-




"""Main module."""
