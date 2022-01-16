import collections
from typing import Counter

t = int(input())

while t:
    s = input()
    num = input()
    list = s.split(num)
    print(int((len(s) - len("".join(list))) / len(num)))

    t -= 1
