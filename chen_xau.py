s1 = input()
s2 = input()
position = int(input())
tmpString = s1[position-1:]
s1 = s1[:position-1] + s2 + tmpString
print(s1)