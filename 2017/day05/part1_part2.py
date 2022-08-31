file=open("./data/5.txt")

original_instructions=[int(line) for line in file.readlines()]

def step_by_step(instructions,part_two=False):
    line=0
    steps=0
    while line<len(instructions):
        jump=instructions[line]
        if jump>=3 and part_two:
            instructions[line]-=1
        else:
            instructions[line]+=1
        line+=jump
        steps+=1
    return steps

print (step_by_step(original_instructions.copy()))
print (step_by_step(original_instructions.copy(),part_two=True))
