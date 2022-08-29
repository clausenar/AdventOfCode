
array=[i[:-1] for i in open("day19_input.txt")]

def find_letters():
    letters=""
    n=0
    row=0
    drow=1
    dcol=0
    col=array[0].index("|")

    while True:
        if drow==1 or drow==-1:
            if array[row][col]=="+" :
                if array[row][col-1]==" ":
                    drow=0
                    dcol=1
                if array[row][col+1]==" ":
                    drow=0
                    dcol=-1
            if array[row][col]==" ":
                break

        elif dcol==1 or dcol==-1:
            if array[row][col]=="+":
                if array[row-1][col]==" ":
                    drow=1
                    dcol=0
                elif array[row+1][col]==" ":
                    drow=-1
                    dcol=0
            if array[row][col]==" ":
                break

        if array[row][col].isalpha():
            letters+=array[row][col]

        col=col+dcol
        row=row+drow
        n+=1

    return letters,n

print ("The identified letters are:",find_letters()[0])
print ("The number of steps are:",find_letters()[1])
