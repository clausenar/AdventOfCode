layers=open("./data/13_test.txt")

def caught(time):
    return (time+depth)%((range-1)*2)==0

hit=0
for line in layers:
    depth,range=int(line.split(":")[0]),int(line.split(":")[1])
    print (depth,range)
    if caught(0):
        hit+=int(depth)*int(range)

print "The severity is",hit
