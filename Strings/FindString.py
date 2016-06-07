String = raw_input()
subString = raw_input()

x = len(subString) -1
L = len(String)
counter = 0

for i in range(0,L):
    if( String[i:i+x+1] == subString):
        counter += 1

print counter

