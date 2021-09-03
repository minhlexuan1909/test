import string

while True:
    s = input().split()
    if (len(s) == 1):
        break
    step = int(s[0])
    letterList = [letter for letter in s[1]]
    # print(step, letterList)

    alphabet = string.ascii_uppercase
    alphabet += '_.'
    for i in range(0, len(letterList)):
        if (letterList[i] >= 'A' and letterList[i] <= 'Z'):
            indexInAlphabet = ord(letterList[i]) - ord('A')
        elif letterList[i] == '_':
            indexInAlphabet = 26
        else:
            indexInAlphabet = 27
        letterList[i] = alphabet[(indexInAlphabet + step) % 28]

    print(''.join(letterList[::-1]))