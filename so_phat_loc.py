t = int(input())

while t:
    s = input()
    if len(s) < 2:
        print("NO")
    elif s[-2] == '8' and s[-1] == '6':
        print("YES")
    else:
        print("NO")
    t -= 1