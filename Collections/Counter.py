from collections import Counter
X = int(raw_input())
shoes = list(map(int,raw_input().split()))
N = int(raw_input())
shoes = Counter(shoes)
sum =0
for i in range(N):
    a = map(int, raw_input().split())
    if shoes [a[0]] != 0 :
        sum += a[1]
        shoes[ a[0] ] = shoes[ a[0] ] - 1
        
print sum  
