import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n, m = [int(x) for x in input().split()]
mat = []
for i in range(0, n):
    mat.append([int(x) for x in input().split()])

prime = []
for i in range(0, n):
    for j in range(0, m):
        if isPrime(mat[i][j]):
            prime.append(mat[i][j])

if len(prime) == 0:
    print("NOT FOUND")
else:
    print(max(prime))  # Print max prime sau nhỡ len = 0 -> k có số
    for i in range(0, n):
        for j in range(0, m):
            if mat[i][j] == max(prime):
                print(f"Vi tri [{i}][{j}]")
