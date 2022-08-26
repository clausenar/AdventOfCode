def spinlock(skip):
    l=[0]
    current=0

    for i in range(1,2018):
        insertion=(current+skip)%len(l)+1
        l.insert(insertion,i)
        current=insertion
    return (l[current+1])
