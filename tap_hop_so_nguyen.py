n, m = [int(num) for num in input().split()]

a = set([num for num in input().split()])
b = set([num for num in input().split()])

s1 = [num for num in a if num in b]
s2 = [num for num in a if num not in b]
s3 = [num for num in b if num not in a]

s1.sort()
s2.sort()
s3.sort()

print(' '.join(s1))
print(' '.join(s2))
print(' '.join(s3))

