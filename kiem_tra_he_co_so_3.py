t = int(input())

while t:
    s = input()
    check = True
    for char in s:
        if char != "1" and char != "2" and char != "0":
            check = False
            break
    print({True: "YES", False: "NO"}[check])
    t -= 1
