"""
A rock
B paper
c scissor

X rock
Y paper
Z scissor

X loose
Y draw
Z win
"""

f=open("./data/02_input.txt")

rule = {"AX":3,"AY":6,"AZ":0,"BX":0,"BY":3,"BZ":6,"CX":6,"CY":0,"CZ":3}
ruleA = {"AX":3,"AY":6,"AZ":0}
ruleB = {"BX":0,"BY":3,"BZ":6}
ruleC = {"CX":6,"CY":0,"CZ":3}
score = {"X":1,"Y":2,"Z":3}
decision = {"X":0,"Y":3,"Z":6}

hands = [i.strip().replace(" ","") for i in f.readlines()]
score_part_1 = [rule[i]+score[i[-1]] for i in hands]

print ("Part 1 score:",sum(score_part_1))

score2 = 0

for key in hands:
    if key[0]=="A":
        card= {i for i in ruleA if ruleA[i]==decision[key[-1]]}
    if key[0]=="B":
        card= {i for i in ruleB if ruleB[i]==decision[key[-1]]}
    if key[0]=="C":
        card= {i for i in ruleC if ruleC[i]==decision[key[-1]]}

    card = "".join(card)[-1]
    
    score2 += decision[key[-1]]+score[card[-1]]
    
print ("Part 2 score:", score2)