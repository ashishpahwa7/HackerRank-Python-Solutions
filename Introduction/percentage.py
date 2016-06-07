N = int(raw_input())

dict = {}

for i in range(N):

    record = raw_input().split(" ")  
    dict[record[0]] = map(float, record[1:4])

      
query_name = raw_input()

marks = dict.get(query_name) 
sum =0
for i in marks:
    sum = sum + i
    
avg = float(sum/3)

print "%.2f"%round(avg,2)

