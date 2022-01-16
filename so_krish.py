arr = [1]
for i in range(1, 10):
    arr.append(arr[i - 1] * i)
t = int(input())
while t:
    n = int(input())
    s = str(n)
    sum = 0
    for c in s:
        sum += arr[int(c)]
    print({True: "Yes", False: "No"}[sum == n])
    t -= 1
