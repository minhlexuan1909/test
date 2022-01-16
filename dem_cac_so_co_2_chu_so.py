from itertools import count


s = input()
listNum = [s[i : i + 2] for i in range(0, len(s), 2)]

appeared = [0] * 100
for num in listNum:
    if appeared[int(num)] == 0 and int(num) >= 10:
        print(num, listNum.count(num))
        appeared[int(num)] = 1
