n,x = [int(num) for num in input().split()]

primeList = []
primeList.append(2)
for i in range(3, 10000):
    check = True
    for num in primeList:
        if i%num == 0:
            check = False
            break
    if check:
        primeList.append(i)
resString = ""
resString += str(x)
for i in range(0, n):
    resString += " " + str(x + primeList[i])
    x+=primeList[i]

print(resString)