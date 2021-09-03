t = int(input())

while t:
    n = input()
    numList = [int(num) for num in n]
    check = True
    if sum(numList) % 10 == 0:
        for i in range(1,len(numList)-1):
            if abs(numList[i]-numList[i-1]) != 2:
                check = False
                break
    else:
        check = False

    print({True: 'YES', False: 'NO'}[check])
    t-=1

