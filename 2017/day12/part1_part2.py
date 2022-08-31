
lib={}
connectors=set()

def count(n):
    connectors.add(n)
    data=open("./data/12.txt")
    for line in data.readlines():
        block=line.split(" ")[0]
        #block=int(block)
        chain=set(line.split(" <-> ")[1].strip().split(", "))
        #chain=int(chain)
        if block in connectors:
            for i in chain:
                if i<block and str(i) not in connectors:
                    connectors.update(chain)
                    count(n)
            connectors.update(chain)
        if chain in connectors:
            connectors.add(block)
            connectors.update(chain)
        lib[block]=chain
    return (connectors)

count('0')

total_list=[]

seen = count(0)
islands = 1
first_island_size = len(seen)-1

for pipe in lib:
    if pipe not in seen:
        pipe_island = count(pipe)
        islands += 1
        seen |= pipe_island

print(first_island_size)
print(islands)
