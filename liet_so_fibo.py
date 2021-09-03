t = int(input())

fibo = [1,1]

for i in range(2,93):
    fibo.append(fibo[i-1] + fibo[i-2])

while t:
    resString = ""
    a,b = [int(num) for num in input().split()]
    for i in range(a,b+1):
        resString += str(fibo[i-1]) + " "
    t-=1
    print(resString)