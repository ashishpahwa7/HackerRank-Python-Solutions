N = int(raw_input())

records = [[] for _ in range(N)]

for i in range(0, N):
    name = raw_input()
    score = float(raw_input())
    records[i]=[name,score]
marks = []
names = []
res = []

marks = [mark for name, mark in records]
names = [name for name, mark in records]

[names.pop(marks.index(x)) for x in marks if x == min(marks)]
marks = [x for x in marks if x != min(marks)]
[res.append(names[i]) for i in range(0,len(marks)) if marks[i]==min(marks)]

res = sorted(res)
for i in res:
    print i
