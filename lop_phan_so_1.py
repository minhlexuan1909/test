import math


class PhanSo:
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        num = math.gcd(self.tu, self.mau)
        tu = self.tu / num
        mau = self.mau / num
        return f"{int(tu)}/{int(mau)}"


arr = input().split()
ps = PhanSo(int(arr[0]), int(arr[1]))
print(ps.rutGon())
