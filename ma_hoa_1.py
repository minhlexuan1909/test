t = int(input())

while t:
    s = input()
    s += '.'
    resString = ""
    countLetter = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            resString += str(countLetter) + s[i-1]
            countLetter = 1
        else:
            countLetter += 1
    print(resString)
    t-=1
