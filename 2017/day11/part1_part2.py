file=open("./data/11.txt")
moves=file.read().strip().split(",")

directions_x={"ne":0.5,"se":0.5,"n":0,"nw":-0.5,"sw":-0.5,"s":0}
directions_y={"ne":0.5,"se":-0.5,"n":1,"nw":0.5,"sw":-0.5,"s":-1}

pos_x,pos_y,max=0,0,0

for move in moves:
    pos_x+=directions_x[move]
    pos_y+=directions_y[move]
    if abs(pos_x)+abs(pos_y)>max:
        max=abs(pos_x)+abs(pos_y)

print ("To get home",abs(pos_x)+abs(pos_y))
print ("Most far away",max)
