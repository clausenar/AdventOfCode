f = open("./data/05_input.txt")

start = f.readlines()
stacks = int(len(start)/3)
all_stacks = [[] for i in range(stacks) ]

for i in start:
    i=i.strip("[").strip("]")
    for key,value in enumerate(i):
        if value.isalpha() and value.isupper():
            all_stacks[key//4].append(value)

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

        
        