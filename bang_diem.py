sma = 1
import math


def my_round(n, ndigits):
    part = n * 10 ** ndigits
    delta = part - int(part)
    # always round "away from 0"
    if delta >= 0.5 or -0.5 < delta <= 0:
        part = math.ceil(part)
    else:
        part = math.floor(part)
    return part / (10 ** ndigits) if ndigits >= 0 else part * 10 ** abs(ndigits)


class HocSinh:
    xepLoai = ""

    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem  # arr

    def getMa(self):
        return self.ma

    def getTen(self):
        return self.ten

    def getDiemTB(self):
        res = 0
        for i in range(0, len(self.diem)):

            if i == 0 or i == 1:
                res += self.diem[i] * 2
            else:
                res += self.diem[i]
        # print(res / 12 * 10)
        # d = decimal.Decimal(res)

        return my_round(res / 12, 1)

    def getXepLoai(self):
        diem = float(self.getDiemTB())
        if diem < 5:
            self.xepLoai = "YEU"
        elif diem < 7:
            self.xepLoai = "TB"
        elif diem < 8:
            self.xepLoai = "KHA"
        elif diem < 9:
            self.xepLoai = "GIOI"
        else:
            self.xepLoai = "XUAT SAC"
        return self.xepLoai

    def getThongTin(self):
        s = ""
        if self.ma < 10:
            s = "0" + str(self.ma)
        else:
            s = str(self.ma)
        return f"HS{s} {self.ten} {self.getDiemTB()} {self.getXepLoai()}"


t = int(input())
listHS = []

while t:
    ten = input()
    diem = [float(x) for x in input().split()]
    hs = HocSinh(sma, ten, diem)
    listHS.append(hs)
    sma += 1

    t -= 1


listHS.sort(key=lambda hs: (-hs.getDiemTB(), hs.getMa()))
# listHS = listHS[::-1]
for hs in listHS:
    print(hs.getThongTin())
