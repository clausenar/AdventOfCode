def solve2(steps):
    cur=0
    for i in range(1,50_000_000):
        cur=(cur+steps)%i+1
        if cur==1:
            second=i
            print ("hit",i)
    return (second)
