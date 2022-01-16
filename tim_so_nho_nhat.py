import re

t = int(input())

while t:
    s = input()
    arr = re.findall("\d+", s)
    arr = [int(x) for x in arr]
    print(min(arr))
    t -= 1
