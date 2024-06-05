#This code is meant to generate a string of random ones and zeros and count how many of the same number occur in a row

import random
from random import randint 
import matplotlib.pyplot as plt

countOfCounts = [0] * 100
allMaxes=[]

for y in range(1000):
    length_of_string = 100
    rand = []

    for x in range (length_of_string):
        numb = randint(0,1)
        rand.append(numb)

    #print(rand)

    placeholder=length_of_string-1
    #test=[1,2,3,4,5,6,7,8,9,10]

    count=1
    seq = []
    for n in range(length_of_string):
        #print(n)
        #print("---------------------------------")
        current_index = n
        next_index = n+1
        if (current_index)==placeholder:
            if TF == 0:
                count = 1
                #print(count)
                seq.append(count)
            else:
                #print(count)
                seq.append(count)
        else:
            if rand[current_index] == rand[next_index]:
                count=count+1
                TF=1
            else:
                #print(count)
                seq.append(count)
                count=1
                TF=0

    #print(seq)

    maxVal = max(seq)
    allMaxes.append(maxVal)
    #print(maxVal)

    for x in range(maxVal+1):
        numbInList = seq.count(x)
        tempAdd = countOfCounts[x] + numbInList
        countOfCounts[x] = tempAdd
    
    #print("I have completed a lap")

#print(countOfCounts)

maxOfMax = max(allMaxes)
#print(maxOfMax)
del countOfCounts[maxOfMax+2:]
print(countOfCounts)

newLength= len(countOfCounts)

#plt.hist(seq)
#plt.show()

xAxis = range(0, newLength)

plt.bar(xAxis, countOfCounts, color='red')
plt.xlabel("Length of Repeat")
plt.ylabel("Instances")
plt.show()

#print("---------------------------------")
#for n in range(length_of_string):
#    print(n)

## sum the numbers in a sim, then at the end divide by the number of 