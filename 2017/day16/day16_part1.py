import string

moves=open("input.txt").read().split(",")
programs=list(string.ascii_lowercase[0:16])

def spin(move,programs):
    n=int(move[1:])
    return programs[-n:]+programs[:-n]

def exchange(move,programs):
    i,j=[int(val) for val in move[1:].split("/")]
    programs[i],programs[j]=programs[j],programs[i]
    return programs

def partner(move,programs):
    i=programs.index(move[1])
    j=programs.index(move[3])
    programs[i],programs[j]=programs[j],programs[i]
    return programs

moves_hash={"s":spin,"x":exchange,"p":partner}

def dance(moves,programs=None):
    while True:
        for move in moves:
            programs=moves_hash[move[0]](move,programs)
        yield "".join(programs)

def solve(moves, programs):
    return next(dance(moves, programs))

print (solve(moves,programs))
