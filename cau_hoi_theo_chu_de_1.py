import re

t = int(input())
s = ""
while t:
    s += input() + "\n"
    t -= 1

list = s.split("\n")
check = False
res = ""
count = 0
# print(list)
for st in list:
    if check == False and st != "":
        res = st
        check = True
    elif check == True and st == "":
        print(f"{res}: {count}")
        check = False
        count = 0
    elif check == True:
        count += 1
