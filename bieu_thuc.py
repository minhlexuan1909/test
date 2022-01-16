t = int(input())
while t:
    s = input()
    i = 1
    st = []
    for char in s:
        if char == "(":
            st.append(i)

            print(i, end=" ")
            i += 1
        elif char == ")":
            print(st[len(st) - 1], end=" ")
            st.pop()
    print()
    t -= 1
