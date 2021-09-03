n = int(input())
numList = (input().split())
# print(numList)
count = 0
for i in range(0, n):
    for j in range(i+1, n):
        if (i < j) and (int(numList[i]) > int(numList[j])):
            count += 1
print(count)

