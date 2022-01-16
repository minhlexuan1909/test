t = int(input())

while t:
    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    maxNum = max(arr)
    for i in range(0, n):
        if arr[i] == maxNum:
            arr.insert(i, m)
            break
    for num in arr:
        if num < 0:
            print(num, end=" ")
    for num in arr:
        if num >= 0:
            print(num, end=" ")
    print()
    # print(arr)
    t -= 1
