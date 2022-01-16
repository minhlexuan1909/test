t = int(input())

while t:
    s = input()
    i = 1
    if len(s) < 3:
        print("NO")
        t -= 1
        continue
    while i < len(s) and s[i] > s[i - 1]:
        i += 1
    while i < len(s) and s[i] < s[i - 1]:
        i += 1
    print({True: "YES", False: "NO"}[i == len(s)])

    t -= 1
