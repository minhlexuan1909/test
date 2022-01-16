n = int(input())

arr = [int(x) for x in input().split()]
arr.sort()
res = []
res.append(arr[-1] * arr[-2] * arr[-3])
res.append(arr[-1] * arr[-2])
res.append(arr[0] * arr[1])
res.append(arr[0] * arr[1] * arr[2])
res.append(arr[0] * arr[1] * arr[-1])  # TH 2 số đầu âm, số cuối dãy dương
res.sort()
print(res[-1])
