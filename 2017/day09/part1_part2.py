stream=open("./data/9.txt").readline()

packages=0
nesting_level=0
garbage=0
i=0

while i<len(stream):
    if stream[i]=="<":
        i+=1
        while stream[i]!=">":
            if stream[i]=="!":
                i+=1
            else:
                garbage+=1
            i+=1
    elif stream[i]=="{":
        nesting_level+=1
    elif stream[i]=="}":
        packages+=nesting_level
        nesting_level-=1
    i+=1

print ("The number of packages are:",packages)
print ("The number of garbage is:",garbage)
