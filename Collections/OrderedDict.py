from collections import OrderedDict
N = int(raw_input())
dic = OrderedDict()
for _ in range(N):
    item,space,quantity = raw_input().rpartition(' ')
    dic[item] = int(dic.get(item,0)) + int(quantity)
    
for key in dic:
    print key,dic.get(key,0)
