t = int(input())

while t:
    n = int(input())
    numList = input().split()
    numList.sort()
    numList.append('x')
    count = 1
    for i in range(0, len(numList)-1):
        if (numList[i] == numList[i+1]):
            count += 1
        else:
            # print(f'count cua {numList[i]} la: {count}')
            if (count % 2 == 0):
                count = 1
            else:
                print(numList[i])
                break
    t-=1