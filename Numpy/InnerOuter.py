import numpy
A = numpy.array((raw_input().split()), int)
B = numpy.array((raw_input().split()), int)

print numpy.inner(A,B)
print numpy.outer(A,B)
