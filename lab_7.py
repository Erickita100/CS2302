 # Ericka Najera Lab 7 MW 10:30-11:50
#Professor Fuentes CS2302
#Lab 7 implement Breath first search and depth first search


#Implementation of disjoint set forest 
# Programmed by Olac Fuentes
# Last modified March 28, 2019
import matplotlib.pyplot as plt
import numpy as np

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
            
def NumSets(S):
    sets = 0
    count = np.zeros(len(S),dtype = int)
    for i in range(len(S)):
        if S[i]<0:
            sets+=1
        count[find(S,i)] +=1
    return sets

        

######################################################################    
# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import random

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)
    
    
    
def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w


        
def findAdjacent(walls,n):
    #returns a list of the adjacent walls to n
    adjacent = []
    #searches the walls and creates a list with the adjacent cells to that index
    for i in walls:
        if i[0]==n:
            adjacent.append(i[1])
        if i[1]==n:
            adjacent.append(i[0])
    return adjacent 


def adjacentList(walls,maze_rows,maze_cols ):
    #creates a 2d array with a the adjacent walls of that index list 
    adj = [ ]
    #for each index it finds the list of that cell in the findadjacent method
    for i in range(maze_rows*maze_cols):
        adj.append(findAdjacent(walls,i))    
    return adj


def findWall(walls,c,r):
    #return the index of the wall that unites c and r
    for i in range(len(walls)):
        if walls[i]==[c,r] or  walls[i] == [r,c]:
                return i
    return None
                


def maze(S,walls,adjacents):
    #asks the user for how many walls to remove
    #displays the approriate term for n-1 walls
    print('Number of cells is:',len(S))
    print('Number of walls is :',len(walls))
    m = int(input("How many walls do you wish to remove? "))
    type(m)
    if m <(len(walls)-1):
        print('A path from source to destination is not guaranteed to exist')
    if m ==(len(walls)-1):
        print("The is a unique path from source to destination ")
    if m>(len(walls)-1):
        print('There is at least one path from source to destination ')
    
    #selets a random cell
    d = random.randint(0,len(S)-1)
    #creates a visited array to store walls as they are popped which is an edge list
    visited =[]
    
    #originally this runs until there one cell 
    #this is modified to remove how many walls the user wants
    for i in range(m):
        #selects a random cell that is adjacent to the current cell
            r = random.randint(0,len(adjacents[d])-1)
            #checks for the union between them
            if find(S,d)!=find(S,adjacents[d][r]):
                #makes a union
                union(S,d,adjacents[d][r])
                #append the wall to the visted
                visited.append(walls.pop(findWall(walls,d,adjacents[d][r])))
                #the adjacent cell becomes the new cell
                d = r
            else:
                #if no other cells are available it gets another random cell
                d =random.randint(0,len(S)-1)
    #returns the edge list or visited cells
    return visited
    
def breathFirstSearch(adj):
        # start with an list of zeros
        visited = np.zeros(len(adj),dtype = int)
        # create a queue 
        queue = [] 
        #the search will start at cell zero
        cell = 0
        #append the cell to the queue and mark as visted with a one
        queue.append(cell) 
        visited[cell] = 1
        while queue: 
            # dequeue and print it
            cell = queue.pop(0) 
            print (cell, end = " ") 
            #if the cell is the top right corner it has reached the end of the maze
            if cell == len(adj)-1:
                break
            # get all adjacent the cell and enqueue
            #mark as visited
            for i in adj[cell]: 
                if visited[i] == 0: 
                    queue.append(i) 
                    visited[i]=1 



def DFSiterative(adj):   
    #create a list all zeros
    visited = np.zeros(len(adj),dtype = int)
    #search starts at zero
    start = 0
    #creates a stack
    stack = []
    #append to the stack and mark as visited
    stack.append(start)       
    visited[0]=1
    #run until stack is empty
    while stack:
        #pops from stack and prints
        cell =  stack.pop( )
        print(cell,end=' ')
        #if the cell is the top right corner it has reached the end of the maze
        if cell == len(adj)-1:
                break
        # get all adjacent the cell and enqueue
        #mark as visited
        for i in adj[cell]: 
                if visited[i] == 0: 
                    stack.append(i) 
                    visited[i]=1 

def DFSRecursive(start,visited,adj,maze):
        #marks the starting cell as visited
        visited[start] = 1
        #appends to a list to record path instead of printing it
        maze.append(start)
        #runs and sends recursively for all adjacent walls
        for i in adj[start]:
            if visited[i]==0:
                DFSRecursive(i,visited,adj,maze)
        
def printdfs(maze,adj):
    #gets the path and prints until is reaches the goal which is the top right corner
    for i in maze:
        print(i,end=' ')
        if i == len(adj)-1:
            break
    
plt.close("all") 
maze_rows = 5
maze_cols = 5

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
adj = adjacentList(walls,maze_rows,maze_cols)

m = maze(S,walls,adj)

adjacentlist=(adjacentList(m,maze_rows,maze_cols))
print()
print('Breath First Search:')
breathFirstSearch(adjacentlist)
print()
print('Depth First Search:')
print('Iterative:')
DFSiterative(adjacentlist)

visited = np.zeros(len(adjacentlist),dtype = int)
dfs =[]
print()
print('Recursive:')
DFSRecursive(0,visited,adjacentlist,dfs)
printdfs(dfs,adjacentlist)

draw_maze(walls,maze_rows,maze_cols) 



