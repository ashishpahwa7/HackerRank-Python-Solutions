from collections import deque
T = int(raw_input())
for i in range(T):
    
    N = int(raw_input())
    n = deque(map(int, raw_input().split()))
    top = max(n)
    while(len(n) > 0):
        if n[0] >= n[-1] and n[0] <= top:
            top = n[0]
            n.popleft()
        elif n[-1] >= n[0] and n[-1] <= top:
            top = n[-1]
            n.pop()
        else:
            break
    if(len(n) == 0):
        print "Yes"
    else:
        print ("No")
