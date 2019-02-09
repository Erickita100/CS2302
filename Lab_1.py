# Ericka Najera Lab 1 MW 10:30-11:50

import numpy as np
import matplotlib.pyplot as plt
import math


def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w)


orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])

# this following tree segments are used to create the three different figures
#they are created my altering the number of repetitons as well as width of the squares

#Square Figure a
plt.close("all") 
fig, ax = plt.subplots()
draw_squares(ax,10,p,.2)
draw_squares(ax,10,p,.1)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares_a.png')

#Square Figure b
plt.close("all") 
fig, ax = plt.subplots()
draw_squares(ax,10,p,.1)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares_b.png')

# Square Figure c
plt.close("all") 
fig, ax = plt.subplots()
draw_squares(ax,70,p,.06)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares_c.png')


def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
      
# this following tree segments are used to create the three different figures
#they are created my altering the number of repetitons as well as width of the circles

        
#circle figure a      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [100,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles_a.png')

 #circle figure b       
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 40, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles_b.png')

 #circle figure c      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 80, [100,0], 100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles_c.png')



#this method is to draw a square and create 4 different squares for each
        
def seperate_squares(ax,n,w,s,origX,origY,sizeX,sizeY,size):
    if n>0:
        
        #this sends the dimentions in order to draw each square
        draw_squares(ax,1,s,w)
        #the num is created with the dimentions of the grid each square is one quarter of the previous one
        num = (size*0.25)
        #this array is created with the new dimentions of the next square and sending it to the next call
        s = np.array([[origX,origY],[origX,sizeY],[sizeX,sizeY],[sizeX,origY],[origX,origY]])
        #in each recursion i changed the dimentions of all the x and y corners according to the num respectively
        seperate_squares(ax,n-1,w,s,origX-num,origY-num,sizeX-(num*3),sizeY-(num*3),size/2)
        seperate_squares(ax,n-1,w,s,origX-num,(origY+(num*3)),(sizeX-(num*3)), sizeY+num,size/2)
        seperate_squares(ax,n-1,w,s,origX+(num*3),origY+(num*3),sizeX+num,sizeY+num,size/2)
        seperate_squares(ax,n-1,w,s,origX+(num*3),origY-num,sizeX+num,(sizeY-(num*3)),size/2)
    
       
        
 #this following segments are used to produce the output and each time incremented the number of repetitons
size = 300  
origin = 0   
   
#1)4squares figure a
s = np.array([[origin,origin],[origin,size],[size,size],[size,origin],[origin,origin]])
plt.close("all") 
fig, ax = plt.subplots()
seperate_squares(ax,3,.9,s,origin,origin,size,size,size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

#4 squares figure b
s = np.array([[origin,origin],[origin,size],[size,size],[size,origin],[origin,origin]])
plt.close("all") 
fig, ax = plt.subplots()
seperate_squares(ax,4,.9,s,origin,origin,size,size,size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

#4 squares figure c
s = np.array([[origin,origin],[origin,size],[size,size],[size,origin],[origin,origin]])
plt.close("all") 
fig, ax = plt.subplots()
seperate_squares(ax,5,.9,s,origin,origin,size,size,size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()



#this method is to draw the circles from one origin


def side_circles(ax,n,center,radius,width):
    if n>0:
        # this draws the circle each time theres a call
        draw_circles(ax,1,center,radius,width)
        # the call changes the x of the origin and the radius to the decrease each time with the width
        side_circles(ax,n-1,[radius*width,100],radius*width,width) 
        
#this following segments are used to produce the output and each time incremented the number of repetitons for circles
 # 2) circle figure a           
plt.close("all") 
fig, ax = plt.subplots()        
side_circles(ax,90,[100,100],100,.5)        
ax.set_aspect(1.0)
ax.axis('off')
plt.show()      

# 2) circle  figure b   
plt.close("all") 
fig, ax = plt.subplots()        
side_circles(ax,50,[100,100],100,.9)        
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

# 2) circle figure c    
plt.close("all") 
fig, ax = plt.subplots()        
side_circles(ax,70,[100,100],100,.95)        
ax.set_aspect(1.0)
ax.axis('off')
plt.show()






#
def binarytree(height,x,y,x2,y2,size,n):
    if n>0:
        plt.plot([x,y],[x2,y2], 'k-')
        binarytree(height,x2,y2,x/2,size-(size//n),size/2,n-1)
        binarytree(height,x2,y2,x/2,size+(size//n),size/2,n-1)


size =12
x = size/2
y = size
height = 3
fig, ax = plt.subplots()
binarytree(height,x,y,size/2,size-(size//height),size,height)
plt.show()
ax.axis('off')









#this method is to draw circles in a cross and keep drawing 5 inside each
def circle_loops(ax,n,x,y,radius,width):
    if(n>0):
        #here i called the draw circles to draw each circle
        draw_circles(ax, 1,[x,y],radius,width)
        #each call is used for each square
        #i divided the radius by three because theres 3 circles of each axis
        #then incremented or decreased  the x and y by the new radius
        circle_loops(ax,n-1,x,y,radius//3,width)
        circle_loops(ax,n-1,(x-(2*(radius//3))),y,radius//3,width)
        circle_loops(ax,n-1,x,(y+(2*(radius//3))),radius//3,width)
        circle_loops(ax,n-1,(x+(2*(radius//3))),y,radius//3,width)
        circle_loops(ax,n-1,x,(y-(2*(radius//3))),radius//3,width)
 
  #this following segments are used to produce the output and each time incremented the number of repetitons
#4 ) inside circles a      
plt.close("all") 
fig, ax = plt.subplots() 
circle_loops(ax,3,100,100,100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()    

#4 ) inside circles b      
plt.close("all") 
fig, ax = plt.subplots() 
circle_loops(ax,4,100,100,100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()      
  

#4 ) inside circles c      
plt.close("all") 
fig, ax = plt.subplots() 
circle_loops(ax,5,100,100,100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()      






