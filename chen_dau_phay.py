s = input()
s = s[::-1]
resString = ""
for i in range(0, len(s),3):
    resString += s[i:(i+3 < len(s)) and i+3 or len(s)] + ','
resString = resString[::-1]
print(resString[1::])