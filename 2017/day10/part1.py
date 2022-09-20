elements=[i for i in range(0,256)]
input_lengths=[102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216]
current_postion=0
skip_size=0


def knot(list,current_postion,skip_size):
    for i in range(len(input_lengths)):
        sublist_2=[elements[t%len(elements)] for t in range(current_postion,current_postion+input_lengths[i])]
        sublist_flipped=sublist_2[::-1]
        for t in range(len(sublist_flipped)):
            elements[(current_postion+t)%len(elements)]=sublist_flipped[t]
        current_postion+=(input_lengths[i]+skip_size)%len(elements)
        skip_size+=1
    return elements

m=knot(input_lengths,0,0)
print (m[0]*m[1])

input_lengths.extend([17, 31, 73, 47, 23,64])

current_postion=0
skip_size=0
for i in range(64):
    input_lengths=knot(input_lengths,current_postion,skip_size)

from functools import reduce
from operator import xor
bits = ('0', '1', '0', '1', '0', '1', '0')


list2="65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22"
list3=[(int(i)) for i in list2.split("^")]
print (list3)
res = reduce(lambda x, y: x ^ y, list3)

print (res)



#print (input_lengths)
