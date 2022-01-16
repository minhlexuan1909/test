t = int(input())

while t:
    num = input()
    sum = 0
    for i in num:
        sum += int(i)
    # print(sum)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
    t -= 1
