t = int(input())

listNum = [int(num) for num in input().split()]

for i in range (1, t+2):
    if i not in listNum:
        print(i)
        break
