n = int(input())

mat = []
for i in range(0, n):
    mat.append(input())

sum = 0
for i in range(0, n):
    countC = 0
    for j in range(0, n):
        if mat[i][j] == "C":
            countC += 1
    sum += int(countC * (countC - 1) / 2)
for j in range(0, n):
    countC = 0
    for i in range(0, n):
        if mat[i][j] == "C":
            countC += 1
    sum += int(countC * (countC - 1) / 2)

print(sum)
