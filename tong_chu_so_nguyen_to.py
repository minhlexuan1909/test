def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


t = int(input())

while t:
    num = input()
    sum = 0
    for i in num:
        sum += int(i)
    # print(sum)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
    t -= 1
