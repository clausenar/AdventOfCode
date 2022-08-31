blocks=open("input_day6.txt").read()
blocks=blocks.strip().split("\t")
blocks=[int(i) for i in blocks]
seen=[]

def cycles():
    cycle=0
    while True:
        cycle+=1
        highest_block_position=blocks.index(max(blocks))
        highest_block_value=max(blocks)
        blocks[highest_block_position]=0
        for q in range(highest_block_value):
            new_position=(highest_block_position+q+1)%len(blocks)
            blocks[new_position]+=1
        if blocks in seen:
            print ("The number of redistribution cycles:",cycle)
            print ("The length of the loop:",len(seen)-seen.index(blocks))
            break
        else:
            seen.append(list(blocks))

cycles()
