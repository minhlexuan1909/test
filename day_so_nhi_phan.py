n = int(input())
numList = [num for num in input().split()]
count = 0
for i in range(0,n-1):
    if (numList[i] != numList[i+1]):
        count += 1

print(count)
