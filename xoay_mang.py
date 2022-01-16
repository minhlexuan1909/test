# Bai chua tinh den TH xoay k > n
t = int(input())
while t:
    n, k = [int(x) for x in input().split()]
    arr = input().split()
    print(" ".join(arr[k::]), " ".join(arr[:k:]))
    t -= 1
