def spinlock(skip):
    l=[0]
    current=0

    for i in range(1,2018):
        insertion=(current+skip)%len(l)+1
        l.insert(insertion,i)
        current=insertion

    for n,value in enumerate(l):
        if value==2017:
            return (l[n+1])
