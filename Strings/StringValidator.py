String = raw_input()

print any(char.isalnum()  for char in String)
print any(char.isalpha() for char in String)
print any(char.isdigit() for char in String)
print any(char.islower() for char in String)
print any(char.isupper() for char in String)
