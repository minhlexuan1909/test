sma = 1
import math
from time import sleep


def my_round(n, ndigits):
    part = n * 10 ** ndigits
    delta = part - int(part)
    # always round "away from 0"
    if delta >= 0.5 or -0.5 < delta <= 0:
        part = math.ceil(part)
    else:
        part = math.floor(part)
    return part / (10 ** ndigits) if ndigits >= 0 else part * 10 ** abs(ndigits)


class KhachHang:
    def __init__(self, ma, ten, chiSoCu, chiSoMoi) -> None:
        self.ma = ma
        self.ten = ten
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi

    def getMa(self):
        return self.ma

    def getTen(self):
        return self.ten

    def getTien(self):
        chiSo = self.chiSoMoi - self.chiSoCu
        tien = 0
        if chiSo <= 50:
            tien = chiSo * 100
            tien = my_round(tien + tien * 2 / 100, 0)
        elif chiSo <= 100:
            tien = 100 * 50 + (chiSo - 50) * 150
            tien = my_round(tien + tien * 3 / 100, 0)
        else:
            tien = 100 * 50 + 150 * 50 + (chiSo - 100) * 200
            tien = my_round(tien + tien * 5 / 100, 0)
        return tien

    def getThongTin(self):
        return f"KH{'%02d' %(self.ma)} {self.ten} {'%0d' %(self.getTien())}"


listKH = []
t = int(input())
while t:
    listKH.append(KhachHang(sma, input(), int(input()), int(input())))
    sma += 1
    t -= 1

listKH.sort(key=lambda x: (-x.getTien(), x.getMa()))
for kh in listKH:
    print(kh.getThongTin())
