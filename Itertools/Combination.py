from itertools import combinations
S = raw_input().split()
Str = sorted(S[0])
k = int(S[1])
for i in range(1,k+1):
    for x in (combinations(Str,i)):
        print str("".join(x))
