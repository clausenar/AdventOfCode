#with open("./src/01_1.txt") as f:
#   lines=f.read()

f=open("./data/01_input.txt")
import os
print (os.getcwd())

nums= (f.read().split("\n\n"))

#print (nums)

lst= [[int(i) for i in t.split()] for t in nums] 

print (lst)
sums=[sum(i) for i in lst]

#print (max(sums))

print (sorted([(i) for i in sums]))
print (sorted([(i) for i in sums])[-1])

print (sum(sorted([(i) for i in sums])[-3:]))