import re

n = int(input())
numList = []
while n:
    s = input()
    numList.extend([int (num) for num in re.findall('[0-9]+', s)])
    n-=1
numList.sort()
for num in numList:
    print(num)
