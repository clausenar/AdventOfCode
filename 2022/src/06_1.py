file = open("./data/06_input.txt")

seq = file.read()

for i in range(len(seq)-3):
    block = seq[i:i+4]
    if len(set(block))==4:
        print ("Marker will start at:",i+4)
        break