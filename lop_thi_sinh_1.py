sma = 1


class ThiSinh:
    def __init__(self, ten, ngaySinh, diem) -> None:
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.diem = diem  # arr

    def getTen(self):
        return self.ten

    def getNgaySinh(self):
        return self.ngaySinh

    def getTongDiem(self):
        return sum(self.diem)


diem = []
ten = input()
ngaySinh = input()
diem.append(float(input()))
diem.append(float(input()))
diem.append(float(input()))

ts = ThiSinh(ten, ngaySinh, diem)
print(f"{ts.getTen()} {ts.getNgaySinh()} {'%.1f' %(ts.getTongDiem())}")
