M = int(raw_input())
A = map(int, raw_input().split(" "))
N = int(raw_input())
B = map(int, raw_input().split(" "))

A = set(A)
B= set(B)

R =  list( (A.difference(B) ).union(B.difference(A)) )
R.sort()
for i in R:
    print i
