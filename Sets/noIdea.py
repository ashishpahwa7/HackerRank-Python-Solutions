Input = map(int, raw_input().split())
N = raw_input().strip().split()
mA = set(raw_input().strip().split())
mB = set(raw_input().strip().split())
happiness = 0
for element in N:
    if(element in mA):
        happiness +=1
    elif element in mB:
        happiness -=1

print happiness
