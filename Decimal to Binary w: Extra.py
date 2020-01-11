##This is the code with a few extra cells

#Libraries
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
    while NewDec <= 15:
        if repeat == 5:
            break
        NewDec = int(input("Enter an integer: "))
        NewDec2 = list(DecToBin(NewDec))
    
        if NewDec > 15:
            print("This will not be added to NewDecList.\n")
        elif NewDec <= 15:
            NewDecList.append(NewDec)
            print("This will be added to NewDecList.\n")
        
        repeat += 1

#Binary list
Results = []

Input = NewDecList

for i in Input:
    Input = ('{num:04b}'.format(num=i))
    Results.append(Input)

length = [1,1,1,1]
Results2 = iter(Results)
Output = [list(islice(Results2, elem)) for elem in length]
ResultList = [[int(i) for i in sub] for i in Output for sub in i]

#Binary array
ResultArray = np.array(ResultList)

#Binary matrix
ResultMatrix = np.matrix(ResultArray)

#Eigenvalues and eigenvectors
w, v = LA.eig(ResultArray)

print("The eigenvalues are: \n", w)
print("\nThe eigenvectors are: \n", v)

#Check to see if matrix is Hermitian
HRMatrix = ResultMatrix.getH()

if np.all(ResultMatrix == HRMatrix):
    print("The matrix is Hermitian.")
else:
    print("The matrix is not Hermitian")

#Check to see if matrix is unitary
UniMatrix = ResultMatrix.dot(HRMatrix)

if np.all(UniMatrix == np.identity(4)):
    print("The matrix is unitary.\n")
else:
    print("The matrix is not unitary.\n")

#Check to see if matrix is normal
NormMatrix1 = ResultMatrix.dot(HRMatrix)

NormMatrix2 = HRMatrix.dot(ResultMatrix)

if np.all(NormMatrix1 == NormMatrix2):
    print("The matrix is normal.\n")
else:
    print("The matrix is not normal.\n")
