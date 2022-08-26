def generators(A,B):
    total=0
    for i in range(40000000):

        A=A*16807%2147483647
        B=B*48271%2147483647

        if bin(A)[-16:] == bin(B)[-16:]:
            total+=1

    return (total)
