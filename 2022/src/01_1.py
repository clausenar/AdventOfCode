
f=open("./data/01_input.txt")

nums= (f.read().split("\n\n"))
lst= [[int(i) for i in t.split()] for t in nums] 
sums=[sum(i) for i in lst]

print (sorted([(i) for i in sums])[-1])

print (sum(sorted([(i) for i in sums])[-3:]))