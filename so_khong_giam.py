t = int(input())

while t:
    s = input()
    index = 0
    check = True
    for num in s:
        if index == 0:
            index += 1
            continue
        if s[index] < s[index-1]:
            check = False
            break
        index += 1
    if check:
        print('YES')
    else:
        print('NO')
    t -= 1