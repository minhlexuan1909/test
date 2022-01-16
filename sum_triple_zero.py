import bisect


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    pos = bisect.bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1


t = int(input())

while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    count = 0
    for i in range(0, len(arr)):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            sum = arr[i] + arr[l] + arr[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                count += 1
                l += 1
    print(count)
    t -= 1
