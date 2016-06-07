import numpy
Rows, Cols = map(int, raw_input().split())

i = numpy.array([raw_input().split() for _ in range(Rows)], int)

print numpy.transpose(i)
print i.flatten()
