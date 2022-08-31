data=open("./data/1.txt").read().strip()

def part1(data):
    sum=0
    for i in range(len(data)):
        look_ahead=i%len(data)
        if data[i]==data[(i+1)%len(data)]:
            sum+=int(data[i])
    print (sum)


def part2(data):
    sum=0
    for i in range(len(data)):
        look_ahead=int(i+len(data)/2)%len(data)
        if data[i]==data[look_ahead]:
            sum+=int(data[i])
    print (sum)

part1(data)
part2(data)
