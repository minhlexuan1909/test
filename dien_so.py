t = int(input())

while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    minNum = min(arr)
    maxNum = max(arr)
    count = 0
    for i in range(minNum, maxNum + 1):
        if i not in arr:
            count += 1
    print(count)
    t -= 1
