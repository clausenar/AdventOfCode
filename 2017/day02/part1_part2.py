def part1():
    data=open("./data/5.txt")
    checksum=0
    for line in data:
        min_val=0
        max_val=0
        numbers=[int(i) for i in line.split("\t")]
        min_val =min(numbers)
        max_val =max(numbers)
        checksum+=max_val-min_val
    print (checksum)

def part2():
    data=open("./data/5.txt")
    checksum=0
    for line in data:
        min_val=0
        max_val=0
        numbers=[int(i) for i in line.split("\t")]
        for i in numbers:
            for t in numbers:
                if t%i==0 and i!=t:
                    checksum+=t/i
    print (checksum)

part1()
part2()
