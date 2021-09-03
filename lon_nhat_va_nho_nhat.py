while True:
    n = int(input())
    if n == 0:
        break
    numList = []
    while n:
        numList.append(int(input()))
        n-=1
    if numList.count(numList[0]) == len(numList):
        print('BANG NHAU')
        continue
    print(min(numList), max(numList))
    