from itertools import permutations
S = raw_input().split()

Str = S[0]
k = int(S[1])
for x in sorted(permutations(Str,k)):
    print "".join(x)

