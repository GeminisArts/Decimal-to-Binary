#Importing libraries
import numpy as np
from numpy import linalg as LA
import itertools
from itertools import islice

#Decimal to binary
def DecToBin(n):
    
    if n<=1:
        return str(n)
    else:
        return DecToBin(n//2) + DecToBin(n%2)

#User input
NewDec = int()
NewDecList = []
repeat = 1

while repeat < 5:
    while NewDec <= 20:
        if repeat == 5:
            break
        NewDec = int(input("Enter an integer: "))
        NewDec2 = list(DecToBin(NewDec))
    
        if NewDec > 15:
            print("This will not be added to NewDecList, try again.\n")
            repeat -= 1
        elif NewDec <= 15 and NewDec >= 0:
            NewDecList.append(NewDec)
            print("This will be added to NewDecList.\n")
        elif NewDec < 0:
            print("This will not be added to NewDecList, try again.\n")
            repeat -= 1
        
        repeat += 1

#Create list
Results = []

Input = NewDecList

for i in Input:
    Input = ('{num:04b}'.format(num=i))
    Results.append(Input)

length = [1,1,1,1]
Results2 = iter(Results)
Output = [list(islice(Results2, elem)) for elem in length]
ResultList = [[int(i) for i in sub] for i in Output for sub in i]

#Create array
ResultArray = np.array(ResultList)
print(ResultArray)

#Create matrix
ResultMatrix = np.matrix(ResultArray)
print(ResultMatrix)
