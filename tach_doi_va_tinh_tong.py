s = input()
res = int(s[:len(s)//2:]) + int(s[len(s)//2::]) 
print(res)
while (res > 10):
    s = str(res)
    res = int(s[:len(s)//2:]) + int(s[len(s)//2::]) 
    print(res)