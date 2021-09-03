numList = []

while len(numList) != 10:
    tmp = [int(num) for num in input().split()]
    numList.extend(tmp)
modded = set([(num % 42) for num in numList])

print(len(modded))
