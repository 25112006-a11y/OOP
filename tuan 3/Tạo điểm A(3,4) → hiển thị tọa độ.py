import math
class diem():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def hienthi(self,toado):
        print(f'{toado}({self.x},{self.y})')
    def diem_doi_xung_qua_0(self):
        return diem(-self.x, -self.y)
    def khoang_cach(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)


diemA=diem(3,4)
diemA.hienthi('A')

bx=float(input('nhap Bx: '))
by=float(input('nhap By: '))
diemB=diem(bx,by)
diemB.hienthi('B')
diemC=diemB.diem_doi_xung_qua_0()
diemC.hienthi('C')
OB=diemB.khoang_cach(diemC)
AB=diemA.khoang_cach(diemB)
print('khoang cach tu B den O la: ',OB)
print('khoang cach tu A den B la: ',AB)