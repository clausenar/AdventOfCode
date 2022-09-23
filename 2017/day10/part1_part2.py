from functools import reduce
from operator import xor

elements=[i for i in range(0,256)]
input_lengths=[102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216]

current_postion=0
skip_size=0

def knot(elements,input_lengths,current_postion,skip_size):
    for i in range(len(input_lengths)):
        sublist_2=[elements[t%len(elements)] for t in range(current_postion,current_postion+input_lengths[i])]
        sublist_flipped=sublist_2[::-1]
        for t in range(len(sublist_flipped)):
            elements[(current_postion+t)%len(elements)]=sublist_flipped[t]
        current_postion+=(input_lengths[i]+skip_size)%len(elements)
        skip_size+=1
        #print (current_postion,skip_size)
    return elements,input_lengths,current_postion,skip_size

m,input_lengths,current_postion,skip_size=knot(elements,input_lengths,0,0)

print ("Multiplication of the first two numbers in the list gives:",m[0]*m[1])

input_lengths= (list(ord(i) for i in "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"))
input_lengths.extend([17,31,73,47,23])

current_postion=0
skip_size=0
elements=[i for i in range(0,256)]

for i in range(64):
    elements,input_lengths,current_postion,skip_size=knot(elements,input_lengths,current_postion,skip_size)

def list_of_list(elements):
    new_list=[]
    for i in range(0,256,16):
        new_list.append(elements[i:i+16])
    return new_list

new_list2=list_of_list(elements)

def XOR(new_list):
    third_list=[]
    for i in new_list:
        #print (i)
        res = reduce(lambda x, y: x ^ y, i)
        third_list.append(res)
    return third_list

third_list=XOR(new_list2)

print ("Knot has of input puzzle:","".join([hex(i).replace("0x","") for i in third_list]))
