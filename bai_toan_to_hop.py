import itertools

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr = list(set(arr))
arr.sort()

l = list(itertools.combinations(arr, k))
l = [list(x) for x in l]
for s in l:
    s = [str(x) for x in s]
    print(" ".join(s))
