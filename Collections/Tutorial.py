from collections import defaultdict
d = defaultdict(list)

n,m = map(int, raw_input().split())
for i in range(1,n+1):
    A = raw_input()
    d[A].append(i)
for i in range(1,m+1):
    B=raw_input()
    if d[B]:
        d[B]=map(str, d[B])
        print ' '.join(d[B])
    else:
        print ('-1')
