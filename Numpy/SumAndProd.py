import numpy

N,M = map(int, raw_input().split())
#A = numpy.array([raw_input().split() for _ in range(N)], int)
#Sum = numpy.sum(numpy.array([raw_input().split() for _ in range(N)], int),axis=0)
print numpy.product(numpy.sum(numpy.array([raw_input().split() for _ in range(N)], int),axis=0))

