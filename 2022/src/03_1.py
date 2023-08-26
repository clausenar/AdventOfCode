f = open ("./data/03_input.txt")
sacks = f.readlines()

lower_cases= list(map(chr, range(97, 123)))
values = [i for i in range(1,27)]

score_case = {key:value for (key,value) in zip(lower_cases,values)}

score = 0

for i in sacks:
    sack= i.strip()
    len_sack = len(sack)
    
    first_sack = sack[0:int(len_sack/2)]
    second_sack = sack[int(len_sack/2):]
   
    letter =  "".join((set(first_sack) & (set(second_sack))))
    if letter.islower():
        score += score_case[letter]
    else:
        score += score_case[letter.lower()]+26

print ("Part 1 score:",score)

new_group =list(zip(*(iter(sacks),)*3))

score =0

for i in new_group:
    sack_1 =  (i[0]).strip()
    sack_2 =  (i[1]).strip()
    sack_3 =  (i[2]).strip()
    letter =  "".join((set(sack_1) & (set(sack_2)) & set(sack_3)))
    if letter.islower():
        score += score_case[letter]
    else:
        score += score_case[letter.lower()]+26

print ("Part 2 score:",score)




