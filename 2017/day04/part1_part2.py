file=open("./data/4.txt")

first=0
second=0

for line in file:
    words=line.split()
    if len(words)==len(set(words)):
        first+=1
    anagrams=["".join(sorted(word)) for word in words]

    if len(anagrams)==len(set(anagrams)):
        second+=1


print ("Valid entries that are not duplicate words:",first)
print ("Valid entries that are not anagrams:",second)
