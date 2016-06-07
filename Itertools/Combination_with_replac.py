from itertools import combinations_with_replacement
S = raw_input().split()

Str = sorted(S[0])
k = int(S[1])
for x in (combinations_with_replacement(Str,k)):
    print str("".join(x))

