s = input()
s = s[::-1]
i = 0
resString = ""
while i < len(s):
    numList = s[i: (i+3 < len(s)) and i+3 or len(s)]
    i+=3
    while len(numList) < 3:
        numList += '0'
    resString += str(int(numList[0])+int(numList[1])*2+int(numList[2])*4)
print(resString[::-1])