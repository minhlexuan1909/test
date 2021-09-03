t = int(input())

while t:
    s = input()
    result = ""
    for letter in s:
        if letter >= '0' and letter <= '9':
            result += result[-1]*(int(letter)-1)
        else:
            result += letter
    print(result)
    t-=1