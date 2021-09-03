t = int(input())

while t:
    n = int(input())
    numList = []
    while n:
        numList.append(int(input()))
        n-=1
    numList.sort()
    numList.append('x')
    count = 1
    maxValue = -1
    result = numList[0]
    for i in range(0, len(numList)-1):
        if (numList[i] == numList[i+1]):
            count+=1
        else:
            if (maxValue < count):
                maxValue = count
                result = numList[i]
            elif (maxValue == count) and numList[i] < result:
                maxValue = count
                result = numList[i]
            count = 1
    print(result)
    t-=1