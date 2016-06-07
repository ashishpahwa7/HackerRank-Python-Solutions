String = raw_input()
newString = ""

for letter in String:
    if letter.isupper():
        newString += letter.lower()
    else:
        newString += letter.upper()

print newString

