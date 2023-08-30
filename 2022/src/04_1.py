file = open('./data/04_input.txt')

pairs = file.readlines()

count = 0
count2 = 0
for i in pairs:
    a_set=set()
    b_set=set()
    
    a,b = i.strip().split(",")
    
    a_start = int(a.split("-")[0])
    a_stop = int(a.split("-")[1])
    b_start = int(b.split("-")[0])
    b_stop = int(b.split("-")[1])
  
    a_set.update(range(a_start,a_stop+1))
    b_set.update(range(b_start,b_stop+1))

    if a_set.union(b_set)==a_set or a_set.union(b_set)==b_set:  
        count +=1

    if len(a_set.intersection(b_set))>0:
        count2 +=1

print (count,count2)
                     
