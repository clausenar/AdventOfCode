import day10
import numpy as np
sum=0
groups=0
array=[]
for i in range(128):
    value=day10.make_hex("hfdlxzhv-"+str(i))
    string=[bin(int(i, 16)).replace("0b","").zfill(4) for i in value]
    string= ("".join(string))
    while len(string)!=132:
        string+="0000"
    sum+="".join(string).count("1")
    data= (list(string))
    array.append([int(i) for i in data])

print (sum)


### second part has problem with binary string at line 3
from scipy.ndimage import label, generate_binary_structure

labeled_array, num_features = label(array)

print (num_features)

print (array[0][:8])
print (array[1][:8])
print (array[2][:8])
print (array[3][:8])
print (array[4][:8])
