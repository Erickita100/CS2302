# Ericka Najera Lab 3 MW 10:30-11:50
#Professor Fuentes CS2302
#Lab 3 based on the implementation of binary trees


#class provided by professor
import numpy as np
import matplotlib.pyplot as plt
import math


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

######################################################################################
        
        
#search module to  search an  item  and print if it is found      
def search(T,k):
    #save the tree into a temperary node
    temp = T
    #if the tree is empty return it is empty
    if T is None:
        print('tree is empty')
        return 
    #while loop to traverse tree
    while temp is not None:
        #if the item is found return and print
        if(temp.item ==k):
            print('Searched',k,':was found')
            return
        #if not then check that current item to see whether to go right or left
        if k< temp.item:
            temp = temp.left
        else:
            temp = temp.right
    print('Searched',k,':Number Not Found')
    

#builds a tree of a sorted list and returns list
def buildtree(L):
    #base case:if the tree is empty the return a none
    if len(L) ==0:
        return None
    #else build the left side of the tree of the first middle of the array
    left = buildtree(L[:len(L)//2]) 
    #the middle becomes the middle item      
    T = BST(L[len(L)//2])
    #the left side connects to the root
    T.left = left
    #repeasts for the right
    right = buildtree(L[(len(L)//2)+1:])
    T.right = right
    return T

#extract the items of a tree into a list
def extract(T, newlist):
    #if there is a left item  recursive call the left
    if T.left is not  None:
        extract(T.left,newlist);
    #append the root to the list in the middle to make it in order
    newlist.append(T.item)
    #call the right side
    if T.right is not None:
        extract(T.right,newlist);
    
    return newlist;

#prints depths of the tree together
def printdepths(T):
    #save the root into a list
    #counter to save the depth it is at
  l = [T]
  counter =0
  #traverse the list while it is not empty
  while l:
      #create another list 
    remaining = list()
    print('Keys at depth',counter,':',end = ' ')
    #travese the items of the list
    for n in l:
        #print that item of the list
      print(n.item,end = ' ')
      #add the left and right to the remaining list
      if n.left: 
          remaining.append(n.left)
      if n.right: 
          remaining.append(n.right)
    counter+=1
    print()
    l = remaining
#draws a binary tree
def tree(ax,n,w,p,size,height,x1,x2,x3,oldy,newY):
    if n>0:
        #decreases the length of x and y axis
        x = size*.5 
        y =(2*size)*(1/height)
        #plots the lines
        ax.plot(p[:,0],p[:,1],color = 'k')
        
        #creates a new arr to send the other values
        p = np.array([[x1,newY],[x2,oldy],[x3,newY]])
        #the values of each point decrease and increasing depending on y and x and left and right
        tree(ax,n-1,w,p,x,height,x1-x,x1,x1+x,newY,newY-y)
        tree(ax,n-1,w,p,x,height,x3-x,x3,x3+x,newY,newY-y)
        #draw a circle in the middle point
        draw_circles(ax,1,[x2,oldy],(80),w)
#mrthod to get the center and radius of the circles
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


def draw_circles(ax,n,center,radius,w):
    if n>0:
        #in each each circle the numbers of the tree will be plotted
        xs=[400,0,800,-200,200,600,1000,-350,-100,100,300]
        ys=[400,0,0,-400,-400,-400,-400,-600,-600,-600,-600]
        t= [10,4,15,2,8,12,18,1,3,5,9,7]
        counter = 0
        for x, y, in zip(xs,ys):
            
            plt.text(x,y,str(t[counter]),color='k', fontsize=12)
            counter+=1
        a,b = circle(center,radius)
        ax.plot(a,b,color='k')
        
        draw_circles(ax,n-1,center,radius*w,w)


    

T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
    
size = 800
height =2
xs=[10]
ys=[2]

p = np.array([[0,0],[size/2,size/2],[size,0]])
plt.close("all") 
fig, ax = plt.subplots()
tree(ax,4,.2,p,size/2,height,0,400,800,400,0)

ax.set_aspect(1.0)
ax.axis('off')
plt.show()
    

    
print('binary tree:')
InOrder(T)
print()
InOrderD(T,'')
print()


search(T,30)
print()

L = [1,2,3,4,5,6,7,8,9,10]
print('build tree of this list')
print(L)
print()
N= None
N =buildtree(L)
InOrderD(N,' ')
print()

newlist=[]
print('Extracted the elements into following list:')
InOrder(T)
print()
m = extract(T,newlist)
print(m)
print()

print('Printing depths:')
printdepths(T)
   

