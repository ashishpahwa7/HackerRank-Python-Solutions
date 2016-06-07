import itertools, operator

k, m = map(int, raw_input().split())
L = [None] * k
for i in range(k):
    L[i] = map(int, raw_input().split()[1:])

print max(reduce(operator.add, map(lambda x: x*x, l))%m for l in list(itertools.product(*L)))
