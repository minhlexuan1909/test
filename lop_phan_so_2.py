import math


class PhanSo:
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau

    def getTu(self):
        return self.tu

    def getMau(self):
        return self.mau

    def tong(self, ps):
        a = self.tu * ps.getMau() + self.mau * ps.getTu()
        b = self.mau * ps.getMau()
        num = math.gcd(a, b)

        return f"{int(a/num)}/{int(b/num)}"


arr = input().split()
ps1 = PhanSo(int(arr[0]), int(arr[1]))
ps2 = PhanSo(int(arr[2]), int(arr[3]))
print(ps1.tong(ps2))
