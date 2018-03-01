from ledread import ledread


def main():
    matrix = ledread.firstLine()
    if matrix:
        finalMatrix = ledread.read(matrix)
        count = check(finalMatrix)
        print("number of lights on at end of sequence: ",count)

def create(x):
   
    matrix = [[False]*(x) for n in range(x)]
    return matrix


def turnOnOrOff(coordsFromX, coordsFromY, coordsToX, coordsToY, x, cmd):
    for i in range(coordsFromX, coordsToX+1):
    
        for j in range(coordsFromY, coordsToY+1):
        
            if x[j][i] == False and (cmd == "turnon" or cmd == "switch"):
                x[j][i] = True
            
            elif x[j][i] == True and (cmd == "turnoff" or cmd == "switch"):
                x[j][i] = False
                
    return x
                
def check(x):
    count = 0
    for i in range(0,len(x)):
        
        for j in range(0, len(x[0])):
            
            if x[i][j] == True:
                
                count+=1
                    
    return count 


    
                
                
                
                
                

# -*- coding: utf-8 -*-




"""Main module."""
