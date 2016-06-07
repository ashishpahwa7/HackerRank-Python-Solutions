from collections import deque
N = int(input())
d = deque()
for i in range(N):
    cmd,*args = input().split()
    getattr(d,cmd)(*args)
    
for x in d:
    print(x,end=' ')
