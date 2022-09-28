import numpy as np

grid_file=open("./data/22.txt")
infinite_grid=[["." for i in range(1000)] for i in range(1000)]
infinite_grid=np.array(infinite_grid)

array=[]
for line in grid_file:
    line=[i for i in line.strip()]
    array.append(line)
array=np.array(array)

def insert_at(big_arr, pos, small):
    x1 = pos[0]
    y1 = pos[1]
    x2 = x1 + small.shape[0]
    y2 = y1 + small.shape[1]
    big_arr[x1:x2,y1:y2] = small
    return big_arr

new_grid=insert_at(infinite_grid,(500,500),array)
array=new_grid

pos_row=512
pos_col=512

dpos_row=-1

burst=0

for i in range(10000):
    if array[pos_row][pos_col]=="#":
        array[pos_row][pos_col]="."
        ###turn right
        if dpos_row==1:
            dpos_row=0
            dpos_col=-1
        elif dpos_row==-1:
            dpos_row=0
            dpos_col=1
        elif dpos_col==-1:
            dpos_col=0
            dpos_row=-1
        elif dpos_col==1:
            dpos_col=0
            dpos_row=1
    elif array[pos_row][pos_col]==".":
        array[pos_row][pos_col]="#"
        burst+=1
        #print ("turn left")
        ###turn left
        if dpos_row==1:
            dpos_row=0
            dpos_col=1
        elif dpos_row==-1:
            dpos_row=0
            dpos_col=-1
        elif dpos_col==-1:
            dpos_col=0
            dpos_row=1
        elif dpos_col==1:
            dpos_col=0
            dpos_row=-1
    pos_row=pos_row+dpos_row
    pos_col=pos_col+dpos_col

print ("The number of burst are:",burst)
