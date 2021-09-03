t = int(input())

while t:
    n = int(input())
    s = input()
    numList = s.split()
    check = False
    for num in numList:
        if numList.count(num) > n/2:
            print(num)
            check = True
            break
    if check == False:
            print('NO')
    t -= 1