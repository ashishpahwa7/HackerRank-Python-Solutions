X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

print [[X,Y,Z] for X in range(X+1) for Y in range(Y+1) for Z in range(Z+1) if X+Y+Z !=N]


