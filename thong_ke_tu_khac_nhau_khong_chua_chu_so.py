import re

t = int(input())

words = []
while t:
    t -= 1
    words.extend(re.findall("[a-zA-Z]+", input().lower()))

setWord = list(set(words))
setWord.sort(key=lambda x: (-words.count(x), x))

for w in setWord:
    if w != "":
        print(w, words.count(w))
