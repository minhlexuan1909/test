s = input()
count = 0
while len(s) != 1:
    count += 1
    l = [ord(char) - ord("0") for char in s]
    # print(sum(l))
    s = str(sum(l))

print(count)
