 # Ericka Najera Lab 8 MW 10:30-11:50
#Professor Fuentes CS2302
#Lab 8 implement backtracking and randomized programming


import random
import numpy as np
from math import *
from mpmath import *

#this method returns a list of lists that compares all the functions with each other
def Identities(F):
    #create a list of lists to store rewsults
    results =[ [] for i in range(len(F)) ]
    #create a for loop to traverse the list of functions
    for i in range(len(F)):
        #create a while loop to check each function with each other
        counter =0
        #append the function we are checking 
        results[i].append(F[i])
        f1 = F[i]
        while counter < len(F):
            #check both functions by evaluating with a random number from -pi to pi
            f2 = F[counter]
            similar = True
            for n in range(1000):
                t = random.randrange(int(-math.pi),int(math.pi))
                y1 = eval(f1)
                y2 = eval(f2)
                if np.abs(y1-y2)>0.0001:
                    similar = False
            counter+=1
            #append if it is true or false
            results[i].append([f2,similar]) 
    return results

def similarties(L):
    #receive the list and print the results accordingly
    for i in range(len(L)):
        print(L[i][0],':')
        print()
        for j in range(1,len(L)):
            print(L[i][j][0],'=',L[i][j][1])
        print()


#return a subset with the acordin sum
def subsetsum(S,last,goal):
    #base case
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    #save result into a variable and traverse the set, goal gets less my the number appended
    res, subset = subsetsum(S,last-1,goal-S[last]) 
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal)
#creates the two sets from the set already created and the initial set 
def split(S,set1):
    #remove the subset from the set
    for i in range(len(set1)):
        if set1[i] in S:
            S.remove(set1[i])
    #return the new two subsets
    print(S,set1)

def Partition(S, n) : 
    #gets the sum of the array
    sum = 0
    #adds each element of the array into the sum
    for i in range(n): 
        sum += S[i] 
    #if the sum is not even then no partition can be made
    if (sum % 2 != 0) : 
        return False
    #sends the set to be divided into a subset with half the sum
    return subsetsum(S,n-1,sum//2) 



S = [2, 4, 5, 9,13] 
print(S)


if Partition(S,len(S))== False:
    print('[]')
else: 
    split(S,set1)
    
    
F = ['sin(t)','cos(t)','tan(t)','mp.sec(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)','sin(t)*sin(t)','1-cos(t)*cos(t)','(1-cos(t))/2','1/cos(t)']
sim = Identities(F)
similarties(sim)
