from collections import OrderedDict

n = int(input())
dic = OrderedDict()

for i in range(n):
    word=input().strip()
    if(word in dic):
        dic[word] +=1
    else:
        dic[word]=1
print(len(dic))
[print(dic[x],end=' ') for x in dic]

