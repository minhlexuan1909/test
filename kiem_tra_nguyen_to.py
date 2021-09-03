import math

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

n,m = [int(num) for num in input().split()]
matrix = []
for i in range(0,n):
    matrix.append([int(num) for num in input().split()])

for i in range(0,n):
    res = ""
    for j in range(0,m):
        if (checkPrime(matrix[i][j])):
            res += '1 '
        else:
            res += '0 '
    print(res)

