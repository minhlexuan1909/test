t = int(input())
arr = []
while t:
    arr.append(input())
    t -= 1

arr = set(arr)
print(len(arr))
