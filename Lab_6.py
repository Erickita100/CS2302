 # Ericka Najera Lab 6 MW 10:30-11:50
#Professor Fuentes CS2302
#Lab 6 implement Disjoint Set Forest to create a maze






#Implementation of disjoint set forest 
# Programmed by Olac Fuentes
# Last modified March 28, 2019
import matplotlib.pyplot as plt
import numpy as np

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

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
    for i in walls:
        if i[0]==n:
            adjacent.append(i[1])
        if i[1]==n:
            adjacent.append(i[0])
    return adjacent 


def adjacents(walls,maze_rows,maze_cols ):
    #creates a 2d array with a the adjacent walls of that index list 
    adj = [ ]
    for i in range(maze_rows*maze_cols):
        adj.append(findAdjacent(walls,i))    
    return adj


def findWall(walls,c,r):
    #return the index of the wall that unites c and r
    for i in range(len(walls)):
        if walls[i]==[c,r] or  walls[i] == [r,c]:
                return i
    return None
                
def path(S):
    #searches a disjoint set list and returns the longest path
    lengths =0
    index = 0
    for s in range(len( S)):
        if len(S[s])>lengths:
            lengths = len(S[s])
            index= s
    p = []
    p.append(S[index][0])
    p+=S[index]
    return p

def roots(S):
    #returns a list of the roots in a disjoint set 
    root = []
    for s in range(len(S)):
        if len(S[s])==1:
            r = S[s][0]
            root.append(r)
    return root

def maze(S,walls,adjacents):
    #generates a random cell to start off
    #collects the adjacent cells and randomly picks a wall
    #makes a union with the two cells 
    #keeps joining the cells until there are no more cells to pick
    #returns the disjoint set forest
    d = random.randint(0,len(S)-1)
    visited =[]

    for i in range(len(S)*2):
        if adjacents[d]!=[]:
            r = random.randint(0,len(adjacents[d])-1)
            if find(S,d)!=find(S,adjacents[d][r]):
                union(S,d,adjacents[d][r])
                walls.pop(findWall(walls,d,adjacents[d][r]))
                visited.append(d)
                r = adjacents[d][r]
                adj = adjacents[d]
                adj2 = adjacents[r]
                cell = r
                adj.remove(r)
                adj2.remove(d)
                if len(adj)==1: 
                    other = adj[0]
                    adj3=adjacents[other]
                    adj3.remove(d)
                    adjacents[other]=adj3
                    adj=[]
                adjacents[d]=adj
                adjacents[r]=adj2
                d = cell
        else:
             d = visited.pop()
    return S
def mazebyHeight(S,walls,adjacents):
     #generates a random cell to start off
    #collects the adjacent cells and randomly picks a wall
    #makes a union with the two cells 
    #keeps joining the cells until there are no more cells to pick
    #returns the disjoint set forest
    d = random.randint(0,len(S)-1)
    visited =[]

    while len(adjacents)>1:
        if adjacents[d]!=[]:
            r = random.randint(0,len(adjacents[d])-1)
            if find(S,d)!=find(S,adjacents[d][r]):
                union_by_size(S,d,adjacents[d][r])
                walls.pop(findWall(walls,d,adjacents[d][r]))
                visited.append(d)
                r = adjacents[d][r]
                adj = adjacents[d]
                adj2 = adjacents[r]
                cell = r
                adj.remove(r)
                adj2.remove(d)
                if len(adj)==1: 
                    other = adj[0]
                    adj3=adjacents[other]
                    adj3.remove(d)
                    adjacents[other]=adj3
                    adj=[]
                adjacents[d]=adj
                adjacents[r]=adj2
                d = cell
        else:
             d = visited.pop()
    return S 
def mazebyCompression(S,walls,adjacents):
     #generates a random cell to start off
    #collects the adjacent cells and randomly picks a wall
    #makes a union with the two cells 
    #keeps joining the cells until there are no more cells to pick
    #returns the disjoint set forest
    d = random.randint(0,len(S)-1)
    visited =[]

    while len(adjacents)>1:
        if adjacents[d]!=[]:
            r = random.randint(0,len(adjacents[d])-1)
            if find_c(S,d)!=find_c(S,adjacents[d][r]):
                union_c(S,d,adjacents[d][r])
                walls.pop(findWall(walls,d,adjacents[d][r]))
                visited.append(d)
                r = adjacents[d][r]
                adj = adjacents[d]
                adj2 = adjacents[r]
                cell = r
                adj.remove(r)
                adj2.remove(d)
                if len(adj)==1: 
                    other = adj[0]
                    adj3=adjacents[other]
                    adj3.remove(d)
                    adjacents[other]=adj3
                    adj=[]
                adjacents[d]=adj
                adjacents[r]=adj2
                d = cell
        else:
             d = visited.pop()
    return S     


plt.close("all") 
maze_rows = 5
maze_cols = 8

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
adj = adjacents(walls,maze_rows,maze_cols)

S= maze(S,walls,adj)
S= dsfToSetList(S)
pa=path(S)
walls.append(pa)
draw_maze(walls,maze_rows,maze_cols) 


