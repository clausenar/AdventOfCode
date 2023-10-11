from collections import defaultdict

lines =[]
path =[]
dirs=defaultdict(int)

file = open ("./data/07_input.txt")

for l in file:
    t = l.split()
    lines.append(t)

for line in lines:
    if line[0]=="$":
        if line[1]=="cd":
            if line[2]=="..":
                path.pop()
            else:
                path.append(line[2])
    elif line[0]!="dir":
        for i in range(len(path)):
            dirs[tuple(path[: i+1])]+=int(line[0])

print (sum(size for size in dirs.values() if size < 100000))

required = 30000000 - (70000000 - dirs[("/",)])

print (min(size for size in dirs.values() if size >= required))





