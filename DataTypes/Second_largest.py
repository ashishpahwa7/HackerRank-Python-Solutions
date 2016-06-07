N = int(raw_input())

arr = sorted( map(int,raw_input().split()),reverse = True)
print  [i for i in arr if i !=max(arr)][0]
