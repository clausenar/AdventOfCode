f = open("./data/05_input.txt")

start = f.readlines()
stacks = int(len(start)/3)
all_stacks = [[] for i in range(stacks) ]

for i in start:
    i=i.strip("[").strip("]")
    for key,value in enumerate(i):
        if value.isalpha() and value.isupper():
            all_stacks[key//4].append(value)

all_stacks2 = all_stacks

for i in start:
    if i.islower():
        _,number,_,from_,_,to_=i.split(" ")
        for r in range(int(number)):
            package = all_stacks[int(from_)-1].pop(0)
            all_stacks[int(to_)-1].insert(0,package)
             
new_string = []

for i in range(len(all_stacks)):
    if len(all_stacks[i])>0:
        new_string.append(all_stacks[i][0])

print ("Answer to first part:","".join(new_string))

f= open("./data/05_input.txt")

start = f.readlines()
stacks = int(len(start)/3)
all_stacks = [[] for i in range(stacks) ]

for i in start:
    i=i.strip("[").strip("]")
    for key,value in enumerate(i):
        if value.isalpha() and value.isupper():
            all_stacks[key//4].append(value)

all_stacks2 = all_stacks

for i in start:
    if i.islower():
        _,number,_,from_,_,to_=i.split(" ")
        package = all_stacks2[int(from_)-1][0:int(number)]
        all_stacks2[int(from_)-1]=all_stacks2[int(from_)-1][int(number):]
        all_stacks2[int(to_)-1]=package+all_stacks2[int(to_)-1]
             
new_string = []

for i in range(len(all_stacks2)):
    if len(all_stacks2[i])>0:
        new_string.append(all_stacks2[i][0])
    
print ("Answer to second part:","".join(new_string))


        