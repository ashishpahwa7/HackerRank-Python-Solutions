String = raw_input()
ic = raw_input().split(" ")

String = String[0:int(ic[0])] + ic[1] + String[int(ic[0])+1:]
print String
