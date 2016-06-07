nA = input()
A = set(map(int, input().split()))
N = int(input())

for i in range(0,N):
    cmd = input().split()
    Set = set(map(int, input().split()))
    getattr(A, cmd[0])(Set)
    
print(sum(A))
