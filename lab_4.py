# Ericka Najera Lab 4 MW 10:30-11:50
#Professor Fuentes CS2302
#Lab 4 based on the implementation of B trees


class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
###############################################################################
        
def height(T):
    #computes the height of the tree which is different from the depth
    #base case if the tree is null then it will return zero
    if T is None:
        return 0
    #if T is a leaf then it returns 1 becaause there height of one
    if T.isLeaf:
        return 1
    #else it recursively calls the tree and adds one
    return 1 + height(T.child[0])

def extractItems(T,extracted):
    #if the root itself is a leaf append all items to the list
    if T.isLeaf:
        for t in T.item:
            extracted.append(t)
    else:
        #if not call all the child in the t.item and append that t.item to the list
        for i in range(len(T.item)):
            extractItems(T.child[i],extracted)
            extracted.append(T.item[i])
        extractItems(T.child[len(T.item)],extracted) 
    return extracted
    
def minAtDepth(T,d):
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return 
    
    #if it has reached that depth returns the first element in the list which is the smallest 
    if d == 0:
        return T.item[0]
    #if both the depth is not reached but T is a leaf it has reached the end of the tree and depth is nonexistent
    if T.isLeaf:
        return
    #if none ifs those of true them call the first child while decreasing the depth
    return minAtDepth(T.child[0],d-1)
        
def maxAtDepth(T,d):
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return 
    #if it has reached that depth returns the last element in the list which is the biggest 
    if d == 0:
        return T.item[-1]
    #if both the depth is not reached but T is a leaf it has reached the end of the tree and depth is nonexistent
    if T.isLeaf:
        return
    #if none ifs those of true them call the first child while decreasing the depth
    return maxAtDepth(T.child[-1],d-1)

def nodesInDepth(T,d):
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return
    #if the depth is at 0 then we will return one for that node
    if d == 0:
        return 1
    #if the t is a leaf and d hasnt reached 0 then return
    if T.isLeaf:
        return 0
    else:
        #save the count while traversing the child of T and return
        count=0
        for i in range(len(T.child)):
            count += nodesInDepth(T.child[i],d-1)
    return count   
            
        
def PrintAtDepth(T,d):
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return 
    #if the depth is zero then print all items in T
    if d == 0:
        for i in range(len(T.item)):
            print(T.item[i],end=' ')
        return
    #if both cases where not reached then either the tree or depth is null
    if T.isLeaf:
        return
    #else call the child of T with the depth decreasing by 1
    else:
        for i in range(len(T.child)):
            PrintAtDepth(T.child[i],d-1)
            
def fullNodes(T):
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return
    #initiate a variable to count
    count = 0
    #if the T is not a leaf traverse the tree
    if not T.isLeaf:
        for i in range(len(T.child)):
            count += fullNodes(T.child[i])
    #if that T is full then count increments
    if len(T.item) == T.max_items:
        count += 1
    return count

def fullLeafNodes(T): 
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return 
     #initiate a variable to count
    count = 0
     #if the T is a leaf and it has reached a max items count is incremented
    if T.isLeaf:
        if len(T.item) == T.max_items:
            return 1
    else:
        #for loop traverses the child items sends the rest of the tree
        for i in range(len(T.child)):
            count =+ fullLeafNodes(T.child[i])
    return count   

def FindDepth(T, k):
    #base case if the tree is null and there is more depth than tree
    if T is None:
        return 
    #if the key is inside that node return 0
    if k in T.item:
        return 0
    #if both cases were not reached then return -1 since it wasnt found
    if T.isLeaf:
        return -1
    #if the item is bigger than the biggest value in T then call that last child in the list
    if k>T.item[-1]:
        d = FindDepth(T.child[-1],k)
    else:
        #if not then check send each node and if it is less then that child send that child list
        for i in range(len(T.item)):
            if k < T.item[i]:
                d = FindDepth(T.child[i],k)
    #if the tree is traversed and key was no found return -1
    if d == -1:
        return -1
    #else return the number of depth +1 because of the then it would increment depth at all
    return d +1


L = [30, 50, 10, 20, 60, 70,100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    Insert(T,i)
     
PrintD(T,'')
print()    

print('The height of the tree is:',height(T))
print()

print('Extracted tree into the following list')
extracted = []
extracted =extractItems(T,extracted)
print(extracted)
print()

depth= 2
print('Min value of depth:',depth,' is ',minAtDepth(T,depth) )
print()
print('Max value of depth:',depth,' is ',maxAtDepth(T,depth) )
print()

print('Number of Nodes in depth', depth, ':',nodesInDepth(T,depth))
print()
print('Printing items in depth:', depth)
PrintAtDepth(T,depth)
print()
print()

print('Printing number of full nodes:',fullNodes(T))
print()
print('Printing number of full leaf nodes:',fullLeafNodes(T))
print()
key = 200
print('Find the depth of key:',key,'at depth:', FindDepth(T,key))