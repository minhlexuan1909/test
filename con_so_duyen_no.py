t = int(input())

while t:
    s = input()
    print({True: "YES", False: "NO"}[s[0] == s[len(s) - 1]])
    t -= 1
