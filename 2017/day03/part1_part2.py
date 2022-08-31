from math import sqrt,floor
import numpy as np

input=325489
dx=0
dy=1
n=floor(sqrt(input))+5
x=n//2
y=n//2
array=np.zeros([n,n])
array[x,y]=1

def update_cursor():
    global x,y,dx,dy
    ### right
    if array[x][y+1]==0 and dy==1 and dx==0 and array[x-1][y+1]!=0:
        y+=1
    ###right turn
    elif array[x][y+1]==0 and dy==1 and dx==0 and array[x-1][y+1]==0:
        y+=1
        dx=-1
        dy=0
    ###up
    elif array[x-1][y]==0 and dy==0 and dx==-1 and array[x-1][y-1]!=0:
        x-=1
    ###up turn
    elif array[x-1][y]==0 and dy==0 and dx==-1 and array[x-1][y-1]==0:
        x-=1
        dx=0
        dy=-1
    ###left
    elif array[x][y-1]==0 and dy==-1 and dx==0 and array[x+1][y-1]!=0:
        y-=1
    ###left turn
    elif array[x][y-1]==0 and dy==-1 and dx==0 and array[x+1][y-1]==0:
        y-=1
        dx=1
        dy=0
    ###down
    elif array[x+1][y]==0 and dy==0 and dx==1 and array[x+1][y+1]!=0:
        x+=1
    ### down return
    elif array[x+1][y]==0 and dy==0 and dx==1 and array[x+1][y+1]==0:
        x+=1
        dx=0
        dy=1
    return (x,y,dx,dy)

def find_position():
    for i in range(2,input+1):
        update_cursor()
        array[x,y]=i
    pos= (np.where(array==input))
    move=abs(pos[0]-n//2)+abs(pos[1]-n//2)
    print ("Steps to access port:",move[0])

find_position()

input=325489
n=floor(sqrt(input))+4
x=n//2
y=n//2
array=np.zeros([n,n])
array[x,y]=1

def find_next():
    for i in range(2,100):
        update_cursor()
        array[x,y]=array[x-1:x+2,y-1:y+2].sum()
        if array[x,y]>input:
            print ("First move larger than puzzle input:",int(array[x,y]))
            break

find_next()
