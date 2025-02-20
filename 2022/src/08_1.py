import numpy as np

file = open ("./data/08_test.txt")

grid = []

for line in file:
    grid.append(list(line.strip()))
    
print (grid)