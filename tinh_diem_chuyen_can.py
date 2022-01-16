class SinhVien:
    def __init__(self, ma, ten, lop, diem) -> None:
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = diem


t = int(input())
listSV = []
for i in range(0, t):
    sv = SinhVien(input(), input(), input(), 0)
    listSV.append(sv)

for i in range(0, t):
    ma, dd = input().split()
    for sv in listSV:
        if sv.ma == ma:
            diem = 10
            for char in dd:
                if char == "v":
                    diem -= 2
                elif char == "m":
                    diem -= 1
            if diem < 0:
                diem = 0
            sv.diem = diem
for sv in listSV:
    print(sv.ma, sv.ten, sv.lop, sv.diem, {True: "KDDK", False: ""}[sv.diem == 0])
