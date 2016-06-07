import numpy
N, M, P = map(int, input().split())

NP = numpy.array([input().split() for i in range(N)], int)
MP = numpy.array([input().split() for j in range(M)], int)

print(numpy.concatenate((NP, MP), axis = 0))
