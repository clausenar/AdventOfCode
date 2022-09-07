data=open("input.txt")

import re
import collections
weight={}
children={}

for line in data:
    parent,n,*child=re.findall(r'\w+',line)
    weight[parent]=int(n)
    children[parent]=tuple(child)

root = set(weight) - {c for cs in children.values() for c in cs}

print ("The root of the programs are:",*root)

def total_weight(parent):
    sub=[total_weight(c) for c in children[parent]]
    if len(set(sub))>1:
        (target,_),(failure,_)=collections.Counter(sub).most_common()
        print (target-failure+weight[children[parent][sub.index(failure)]])
        return weight[parent]+sum(sub)
    return weight[parent]+sum(sub)

total_weight(*root)
