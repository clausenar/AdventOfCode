input = open("./data/8.txt")
import operator

ops = {
    '<' : operator.lt,
    '>' : operator.gt,
    '==' : operator.eq,
    '!=' : operator.ne,
    '<=' : operator.le,
    '>=' : operator.ge}

register={}
max_value=0
commands=[i.split() for i in input.readlines()]

for line in commands:
    find_value=register.get(line[4],0)
    if ops[line[5]](int(find_value),int(line[6])):
        register[line[0]]=register.get(line[0],0)+(int(line[2]) if line[1]=='inc' else -int(line[2]))
        max_value=max(register[line[0]],max_value)

print ("The final max value is",max(register.values()))
print ("The all time highest value is",max_value)
