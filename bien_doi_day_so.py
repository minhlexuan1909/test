while True:
    numList = [int(x) for x in input().split()]
    # print(numList)
    if numList.count(0) == 4:
        break
    step = 0
    while numList.count(numList[0]) != 4:
        # print(numList)
        firstNum = numList[0]
        for i in range(0,3):
            numList[i] = abs(numList[i]-numList[i+1])
        numList[3] = abs(numList[3]-firstNum)
        step += 1
    print(step)