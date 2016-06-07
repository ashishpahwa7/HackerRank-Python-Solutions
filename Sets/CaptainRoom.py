K = int(input())

rooms = list(map(int, input().split()))
rSet = set(rooms)

print( (K*sum(rSet) - sum(rooms))//(K-1) )
