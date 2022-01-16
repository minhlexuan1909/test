n = int(input())

arr = []
while len(arr) != n:
    numList = [int(x) for x in input().split()]
    arr.extend(numList)

maxNum = max(arr)
check = True
for i in range(1, maxNum + 1):
    if i not in arr:
        check = False
        print(i)

if check:
    print("Excellent!")
