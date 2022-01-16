t = int(input())

while t:
    num = input()
    sum = 1
    for i in num:
        if int(i) != 0:
            sum *= int(i)
    print(sum)
    t -= 1
