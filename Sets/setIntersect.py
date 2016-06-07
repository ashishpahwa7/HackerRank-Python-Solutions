n = input()
E = set(map(int, input().split()))
b = input()
F = set(map(int, input().split()))

count = E.intersection(F)

print(len(count))
