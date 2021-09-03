t = int(input())

while t:
    num = input()
    if num.count('4') + num.count('7') == len(num):
        print("YES")
    else: 
        print("NO")
    t -= 1

