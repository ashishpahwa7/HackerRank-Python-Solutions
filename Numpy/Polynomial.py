import numpy
P = numpy.array(raw_input().split(),float)
x = int(raw_input())
print numpy.polyval(P, x)  


