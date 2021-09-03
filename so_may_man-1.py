s = input()

numLuck = s.count('4') + s.count('7')

if numLuck == 4 or numLuck == 7:
    print("YES")
else:
    print("NO")