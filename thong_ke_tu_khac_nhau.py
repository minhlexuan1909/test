import re
from typing import Counter

t = int(input())

words = []
while t:
    words.extend(re.findall("[a-z0-9]+", input().lower()))
    t -= 1

words = list(Counter(words).items())
words.sort(key=lambda x: (-x[1], x[0]))
for k, v in words:
    print(k, v)
