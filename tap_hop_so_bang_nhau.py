n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

setA = list(set(a))
setB = list(set(b))
setA.sort()
setB.sort()
print({True: "YES", False: "NO"}[setA == setB])
