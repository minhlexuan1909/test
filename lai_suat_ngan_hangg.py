t = int(input())

while t:
    n,x,m = [float(num) for num in input().split()]
    # n = a[0]
    # x = a[1]
    # m = a[2]
    count = 0
    while n < m:
        n*=(1+x/100)
        count+=1
    print(count)
    t-=1