t = int(input())

while t:
    s = input()
    letterList = []
    letterList = [letter for letter in s]
    letterList.sort()
    index = 0
    sumNum = 0
    while letterList[index] >= '0' and letterList[index] <= '9':
        sumNum += int(letterList[index])
        index+=1
    resString = ""
    for i in range(index, len(letterList)):
        resString += letterList[i]
    resString += str(sumNum)
    print(resString)
    t-=1

