def sangNguyenTo():
    l = [1] * 100001
    l[0] = 0
    l[1] = 0
    for i in range(2, 100001):
        if l[i] == 0:
            continue
        for j in range(i * i, 100001, i):
            l[j] = 0
    return l


l = sangNguyenTo()
arr = []
for i in range(13, len(l)):
    if l[i] == 1:
        s = str(i)
        s = s[::-1]
        # print(i, s)
        if l[int(s)] == 1 and i < int(s):
            arr.append(i)
# arr = list(set(arr))
# arr.sort()
t = int(input())
while t:
    n = int(input())
    for i in range(0, len(arr)):
        s = str(arr[i])
        s = s[::-1]
        num = int(s)
        if arr[i] < n and num < n:
            print(arr[i], num, end=" ")
    print()
    t -= 1
