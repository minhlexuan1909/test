import re

t = int(input())

while t:
    s = input()
    arr = [int(x) for x in re.findall("\d+", s)]
    print(max(arr))
    t -= 1
