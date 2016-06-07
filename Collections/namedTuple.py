from collections import namedtuple
N = int(raw_input()) ; cnames =','.join(raw_input().split()) ;sum=0
records = namedtuple('records',cnames)
for i in range(N):
    hede = (raw_input().strip().split())
    grade = records(*hede)
    sum += float(grade.MARKS)
print sum/N
