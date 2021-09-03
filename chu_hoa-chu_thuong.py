s = input()
countLower = 0
countUpper = 0
for letter in s:
    if letter >= 'A' and letter <= 'Z':
        countUpper+=1
    else:
        countLower+=1
if (countLower >= countUpper):
    print(s.lower())
else:
    print(s.upper())