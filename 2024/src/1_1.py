from collections import Counter

list1=[]
list2=[]
length = 0
similarity = 0

with open("./1.txt") as f:
    for line in f:
        list1.append((line.split("   ")[0]))
        list2.append((line.split("   ")[1]).strip())

list1.sort()
list2.sort()

for i in range(len(list1)):
    length += abs(int(list1[i])-int(list2[i]))

print ("Solution to problem #1 is:",length)

items1= Counter(list1)
items2= Counter(list2)

for i in list1:    
    similarity += int(i)*items2[(i)]

print ("Solution to problem #2 is:",similarity)

