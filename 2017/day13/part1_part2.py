def ride(time,clean):
    hit_rate=0
    hit=False
    layers=open("./data/13.txt")
    for line in layers:
        depth,range=int(line.split(":")[0]),int(line.split(":")[1])
        if (time+depth)%((range-1)*2)==0:
            hit=True
            if clean:break
            hit_rate+=int(depth)*int(range)
    return hit_rate,hit

print("The severity is",ride(0,False)[0])

time=0
while ride(time,True)[1]==True:
    time+=1
print ("The delay time is",time)
