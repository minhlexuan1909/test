n = int(input())
arr = []
while len(arr) != n:
    arr.extend([int(x) for x in input().split()])
chan = [x for x in arr if x % 2 == 0]
le = [x for x in arr if x % 2 != 0]
chan.sort()
le.sort()
chanInd = 0
leInd = len(le) - 1

for i in range(0, n):
    if arr[i] % 2 == 0:
        print(chan[chanInd], end=" ")
        chanInd += 1
    else:
        print(le[leInd], end=" ")
        leInd -= 1
