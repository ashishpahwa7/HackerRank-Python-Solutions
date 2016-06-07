N = int(raw_input())

L =[]

for i in range(0,N):

    args = raw_input().split(" ")
    if len(args) > 0:
        if args[0] == "insert":
            L.insert(int(args[1]),int(args[2]))
        elif args[0] == "append":
            L.append(int(args[1]))
        elif args[0] == "extend":
            L.extend(int(args[1]))
        elif args[0] == "remove":
            L.remove(int(args[1]))
        elif args[0] == "pop":
            L.pop()
        elif args == "index":
            L.index(int(args[1]))
        elif args[0] == "count":
            L.count(int(args[1]))
        elif args[0] == "sort":
            L.sort()
        elif args[0] == "print":
            print L
        elif args[0] == "reverse":
            L.reverse()

