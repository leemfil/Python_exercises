tekst = input()
versleuteld = ""

for char in tekst:
    if char == 'z':
        versleuteld += '*'
    elif char == 'Z':
        versleuteld += '+'
    elif char.isalpha():
        versleuteld += chr(ord(char) + 1)
    else:
        versleuteld += char

print(versleuteld)
