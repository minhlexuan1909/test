t = int(input())

while t:
    s = input()
    reverseWord = s[::-1]   

    check = True
    for i in range(1, len(s)):

        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(reverseWord[i])-ord(reverseWord[i-1])):
            check = False
            break
    print({True: 'YES', False: 'NO'}[check])
    t-=1

