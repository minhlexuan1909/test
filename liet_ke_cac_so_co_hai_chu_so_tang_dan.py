s = input()

arr = [s[i : i + 2] for i in range(0, len(s), 2)]
if (len(arr[len(arr) - 1])) == 1:
    arr.pop()
arr = list(set(arr))
arr.sort()
arr = [str(x) for x in arr]
print(" ".join(arr))
