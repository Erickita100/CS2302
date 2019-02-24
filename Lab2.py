# Ericka Najera Lab 2 MW 10:30-11:50


import random
import time;

class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
    
        
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    #checks if the list is empty and returns a boolean
    if L.head == None:
        return True
    return False  

def buildlist(L,n):
    #builds a list base on n (number of nodes)
    for i in range(n):
        #each item will be a randome number
        num = random.randint(1,101)
        #if the list is empty it becomes the head
        if IsEmpty(L):
            L.head = Node(num)
            L.tail = L.head
        #else the next item after the last item become a new node
        else:
            L.tail.next = Node(num)
            L.tail = L.tail.next
            
            
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line

def getlength(L):
    #returns length of a list
    #saves to now loose the head
     temp = L.head
     counter =0
     #each loop increments counter is a node is not null
     while temp is not None:
        counter +=1
        temp = temp.next
     return counter
 
def getmid(L):
    #returns the middle of the list
    temp = L.head
    counter = 0
    #the counter will go till the middle node and return it
    while counter!= (getlength(L)//2):
        temp = temp.next
        counter+=1
        
    return temp.item

def copylist(L,newlist):
    #makes a new copy of the list
    temp = L.head
    newlist.head = Node(temp.item)
    newlist.tail = newlist.head
    temp=temp.next
    for i in range(getlength(L)-1):
        newlist.tail.next = Node(temp.item)
        newlist.tail = newlist.tail.next
        temp=temp.next

def swapnum(prev,curr):
    #swaps node with the next one
    temp=prev.item
    prev.item = curr.item
    curr.item = temp
    
def compare(L):
        #compares a node to the next one 
        if L.item > L.next.item:
            return True
        else:
            return False    
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next  
        
def bubblesort(L):
    #if the list is less than 1 it will return the head
    if getlength(L)<1:
        return L.head.item
    else:
        sorted = False
        temp = L.head
        #in each swap sorted will become false and until the list is sorted
        while sorted is False:
            sorted = True
            current=temp
            #the loop goes through the list and it will check and swap if necessary
            while current is not None and current.next is not None:
                if compare(current):
                    swapnum(current,current.next)
                    sorted = False
                current = current.next
        #returns the middle node of the sorted list        
        midnum = getmid(L)
        return midnum
            
            
def quicksort(L):
    #base case
    if getlength(L)>1:
        #the pivot will always be the first node
        pivot = L.head.item
        L1 = List()
        L2 = List()
        #the temp is created to not loose the head of L
        temp = L.head.next
        while temp is not None:
            #if the item is smaller than the pivot it will append to left or bigger to the right
            if temp.item<pivot:
                Append(L1,temp.item)
            else:
                Append(L2,temp.item)
            temp=temp.next
        #append the pivot the left side
        Append(L1,pivot)
        #call recursion for each side
        quicksort(L1)
        quicksort(L2)
        #the head will be the head of the left and the tail the last item of the left
        L.head = L1.head
        L.tail = L1.tail
        #attach the head of right to the last node of left
        L.tail.next =L2.head
        #the tail of the right will become the  new tail 
        L.tail = L2.tail
        #get the middle of the new list and return
        midnum = getmid(L)
        return midnum

def prepend(L,x):
    #inserts node at begginning of list
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        new_node = Node(x) 
        new_node.next = L.head 
        L.head = new_node 

def fastquicksort(L):
    #quicksort with only one recursion happening at a time
    #same first steps as normal quicksort
    if getlength(L)>1:
        pivot = L.head.item
        L1 = List()
        L2 = List()
        temp = L.head.next
        while temp is not None:
            if temp.item<pivot:
                Append(L1,temp.item)
            else:
                Append(L2,temp.item)
            temp=temp.next
        Append(L1,pivot)
        #if the left side is bigger than the left it will forget the other list
        if getlength(L1)>getlength(L2):
            quicksort(L1)
         #if the right is bigger send that list instead   
        else:
            quicksort(L2)
        #this part is the same as the quick sort attachment of the lists
        L.head = L1.head
        L.tail = L1.tail
        L.tail.next =L2.head
        L.tail = L2.tail
        midnum = getmid(L)
        return midnum
    
    
def seperate(L):
    #splits the list into two and returns two new lists
    if L.head is None or L.head.next is None:
        left = L
        right = None    
    else:
        left = List()
        right= List()
        temp = L.head
        #go through the list using the length
        for i in range(getlength(L)):
            #if the index is less than the middle all nodes will be on the left
            if i < (getlength(L)//2):
                Append(left,temp.item)
            #after middle all nodes go the right
            else:
                Append(right,temp.item)
                
            temp = temp.next
        
    return left,right   
  
def merge(a,b):
    result = List()
    a= a.head
    b=b.head
    #go through both lists 
    while a is not None or b is not None:
        #if the one is none then append the remaining of the other list
        if a is None:
            Append(result,b.item)
            b=b.next
        elif b is None:
            Append(result,a.item)
            a=a.next
        else:
            #if both exist check the item
            #append the smaller node first
            if a.item < b.item:
                Append(result,a.item)
                a = a.next
            else:
                Append(result,b.item)
                b = b.next
    return result
def mergesort(L):
    #base case
    if L is None or L.head.next is None:
        return L
    #split the list into two
    left, right = seperate(L)
    #save the recursion for each side
    left = mergesort(left)
    right = mergesort(right)
    #returns the list after they get merged together
    return merge(left, right)    
    
    
print("\n")        
L = List()
buildlist(L,10)
print('original list:')
Print(L)
print("\n")

BS=List()
copylist(L,BS)
start = time.time_ns()
bubblesort(BS)
end = time.time_ns()
print('time in nano seconds',end-start)
print('List after bubblesort:')
Print(BS)
print('Middle index')
print(bubblesort(BS))
print("\n")

MS=List()
copylist(L,MS)
start = time.time_ns()
MS=mergesort(MS)
end = time.time_ns()
print('time in nano seconds',end-start)
print('List after mergesort:')
Print(MS)
print('Middle index')
print(getmid(MS))
print("\n")


QS = List()
copylist(L,QS)
start = time.time_ns()
quicksort(QS)
end = time.time_ns()
print('time in nano seconds',end-start)
print('List after quicksort:')
Print(QS)
print('Middle index')
print(quicksort(QS))
print("\n")

FS=List()
copylist(L,FS)
start = time.time_ns()
fastquicksort(FS)
end = time.time_ns()
print('time in nano seconds',end-start)
print('List after faster quicksort:')
Print(FS)
print('Middle index')
print(fastquicksort(FS))
print("\n")

print('original list once again:')
Print(L)








    