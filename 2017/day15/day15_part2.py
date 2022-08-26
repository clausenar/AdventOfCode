def independent_generators(A,B):
    total=0
    list_A=[]
    list_B=[]
    mind_length=0
    while mind_length<5e6:
        A=A*16807%2147483647
        B=B*48271%2147483647

        if A%4==0:
            list_A.append((A))
        if B%8==0:
            list_B.append((B))

        mind_length=min(len(list_A),len(list_B))

    for i in range(5000000):
        if bin(list_A[i])[-16:] == bin(list_B[i])[-16:]:
            total+=1
    return total
