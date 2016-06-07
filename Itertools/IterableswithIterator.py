from itertools import *
N = input()
L = sorted(raw_input().split())

K = input()
comb = set(combinations(xrange(N),K))

s = {x for x in comb if L[x[0]] == 'a'}

print 1.*len(s)/len(comb)
