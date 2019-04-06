# Ericka Najera Lab 5 MW 10:30-11:50
#Professor Fuentes CS2302
#Lab 5 implementing hash tables and binary search tree to store words and embeddings to find similarities between words


import numpy as np
import math
import time

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        self.num_items=0
        
#doubles the size of the hash table
def doubleSize(H):
    #create a new hash table with twice the length +1
    H2 = HashTableC((len(H.item)*2)+1)
    #traverse the old hash table
    for i in range(len(H.item)):
        for a in H.item[i]:
            #for every index traverse the lists and insert into new hash table
            InsertC(H2,a[0],a[1])
    return H2
#counts number of empty lists in hash table
def emptyLists(H):
    count =0
    #traverse hash table and if that is empty increment count
    for h in H.item:
        if h == []:
            count+=1
    return count
#deviation of the lengths of the lists
def deviation(H):
    lengths =[]
    #get lengths of each index in hash table
    for h in range(len(H.item)):
        lengths.append(len(H.item[h]))
    #get the sum of the lengths
    sum = 0
    for l in lengths:
        sum +=l
    #get average of the sum
    mean = sum/len(lengths)
    #subtract the mean of each length and sqaure it
    for x in lengths:
         x= x - mean
         x = x * x
    #get sum again of the new lengths
    sum = 0
    for a in lengths:
        sum +=a
    #get mean again and square root
    mean = sum/len(lengths)
    mean = math.sqrt(mean)           
    return mean
         
         
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    if loadFactor(H)==1:
        H = doubleSize(H)
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
    H.num_items+=1
    return H

def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1

#find the vakue of the word in order to get a value to store into hash table
def h(s,n):
    r=0
    for c in s:
        r = (r*n+ord(c))%n
    return r

#computes the load factor
def loadFactor(H):
    return H.num_items//len(H.item)    

def buildhash(f):
    #creates a hash table
    H=HashTableC(3)
    print('Hash table stats:')
    print('Initial table size:',len(H.item))
    #read the globe file
    for x in f:
        #save the line and split after space
        line = x
        text = line.split(" ") 
        #save the word seperately
        word = text[0]
        #traverse the line and create a np array
        i = 0
        embed = np.empty([50], dtype=float)
        #save the values of the line after the first word
        for j in range(1,len(text)):
            embed[i]=text[j]
            i +=1  
        #insert the word and embedding into the hash table
        H=InsertC(H,word,embed)
    return H
   
#prints the similarities of the two words in file
def similarities(H,file):
    #traverse the file with words
    print('Reading word file to determine similarities')
    print()
    print('Word similarities found:')
    print()
    for x in file:
        #build list with two words
        words = x.split(',')
        #gets rid of the /n
        words[1] = words[1].replace('\n','')
        #find the two words seperatly in the hash table
        word1 = FindC(H,words[0])
        word2 = FindC(H,words[1])
        #e0 *e1 is the sum of the the profuct of u and v values 
        top= np.sum(word1[2]*word2[2])
        
        #|e0||e1| is the square root of the  sum of the product u and v squared
        bottom = (math.sqrt(np.sum(word1[2]*word1[2]))*math.sqrt(np.sum(word2[2]*word2[2])))
        
        #print the similarity and reduces the float to only 5 digits
        print('Similarity',words,'=',round((top/bottom),5))
    print()
##############################################################################
class BST(object):
    # Constructor
    #item becomes an array
    def __init__(self,item=[],left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right 
#reads file and creates a binary search tree
def buildtree(file):
    T = None
    #creates count of how many nodes in the tree
    num_Nodes=0
    #reads globe file
    for x in file:
        line = x
        #creates a list of each line
        text = line.split(" ") 
        word = text[0]
        #gets the word and get the value of that word
        val = value(word)
        i = 0
        #create an np.array of length 50
        embed = np.empty([50], dtype=float)
        #traverse the line and input the floats after the word
        for j in range(1,len(text)):
            embed[i]=text[j]
            i +=1  
        #insert them into the tree with the item being a list including the value, word and embedding
        T=Insert(T,[val,word,embed])
        #increase number of nodes after each insert
        num_Nodes+=1
    print('Number of Nodes:',num_Nodes)
    return T    
#read file of words and print the similarties
def similarT(T,file):
    #read the file of words
    for x in file:
        #build list with two words
        words = x.split(',')
        #gets rid of the /n
        words[1] = words[1].replace('\n','')
        #find the two words seperatly in the hash table
        word1 = find_word(T,words[0])
        word2 = find_word(T,words[1])
        #e0 *e1 is the sum of the the profuct of u and v values 
        top= np.sum(word1[2]*word2[2])
        #|e0||e1| is the square root of the  sum of the product u and v squared
        bottom = (math.sqrt(np.sum(word1[2]*word1[2]))*math.sqrt(np.sum(word2[2]*word2[2])))
        #print the similarity and reduces the float to only 5 digits
        print('Similarity',words,'=',round((top/bottom),5))
        
#insert item into the tree using the value of the word        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    #compares the value of the word in order to sort them
    elif T.item[0] > newItem[0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T
#returns height of the tree
def height(T):
    if T is not None:
        #recursive calls both left and right tree
        #keeps the biggest side and adds one each time
        return 1 + max([height(T.left),height(T.right)])
    return -1
    
        
#find the words and return that node
def find_word(T,k):
    #create a temp variable
    temp = T
    #traverse the tree 
    while temp is not None:
        #if the the value of the word equal the value of k and the word equals the word return that node
        if temp.item[0]==value(k) and temp.item[1] == k :
            return temp.item
        #if not check the value and send the left or right tree
        elif temp.item[0]>value(k):
            temp = temp.left
        else:
            temp = temp.right
    return None

#returns the value of the word
def value(word):
    #gets the ascii code for each letter
    num =[ord(c) for c in word]
    count =0
    #adds all the numbers for each other and returns the sum
    for a in num:
        count +=a
    return count
#####################################################################
    
file = open("glove.6B.50d.txt", "r")
words = open('words.txt','r')


chosen = input('Chose 1 for binary search and 2 for hash tables:')
print()
type(chosen)
if chosen=='1':
    start = time.time()
    print('you picked binary tree')
    print()
    print('Building binary search tree:')
    print()
    startbuild = time.time()
    T=buildtree(file)
    endbuild = time.time()
    print('Height:', height(T))
    print('Running time for binary search tree construction:',endbuild-startbuild)
    print()
    print('Reading word file to determine similarities')
    print()
    print('Word similarities found:')
    print()
    similarT(T,words)
    end = time.time()
    print()
    print('Running time for binary search tree query processing:',end - start)
elif chosen =='2':
    start = time.time()
    print('you picked hash tables')
    print()
    print('Building hash table with chaining:')
    print()
    startbuild = time.time()
    H=buildhash(file)
    endbuild = time.time()
    print()
    print('Total number of elememts:',H.num_items)
    print('Final table size:',len(H.item))
    print('Load factor:',loadFactor(H))
    dev= deviation(H)
    empty =emptyLists(H) 
    print('Percent of empty lists:',round((empty/len(H.item)*100),2),'%')
    print('Standard deviation:',dev)
    print()
    print('Running time for hash table construction:',endbuild- startbuild)
    print()
    similarities(H,words)
    end = time.time()
    print('Running time for hash table query processing:',end -start)
else:
    print(' you did not choose 1 or 2')
file.close()
words.close()
