t = int(input())

while t:
    num = input()
    check = True
    for i in range(0, len(num), 2):
        if num[i] != num[0]:
            check = False
    for i in range(1, len(num), 2):
        if num[i] != num[1]:
            check = False

    print({True: "YES", False: "NO"}[check])

    t -= 1
