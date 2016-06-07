from itertools import product
A = map(int, input().split())
B = map(int, input().split())
L = [A,B]

for element in product(*L):
    print(element,end=" ")
