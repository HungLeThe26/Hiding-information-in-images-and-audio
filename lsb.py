class ThiSinh:
    def __init__(self,ma,ten,ly_thuyet,thuc_hanh):
        self.ma =ma
        self.ten = ten
        self.ly_thuyet = ly_thuyet / 10
        self.thuc_hanh = thuc_hanh / 10
        self.diem_tb = round((self.ly_thuyet + self.thuc_hanh) /2 ,2)
        self.xep_loai = self.get_xep_loai
    def get_xep_loai(self):
        if self.diem_tb < 5 :
            return "TRUOT"
        elif self.diem_tb <= 8 :
            return "CAN NHAC"
        elif self.diem_tb <=9.5:
            return "DAT"
        else: 
            return "XUAT SAC"
        
def __lt__(self, other):
    return self.diem_tb > other.diem_tb

def __str__(self):
    return f"{self.ma} {self.ten} {self.diem_tb:.2f} {self.xep_loai}"

n = int(input())
thisinh_list= []

for i in range(1, n+1):
    ten = input().strip()
    ly_thuyet= float(input())
    thuc_hanh = float(input())
    ma = f"TS{str(i).zfill(2)}"
    ts = ThiSinh(ma, ten,ly_thuyet,thuc_hanh)
    thisinh_list.append(ts)


for ts in thisinh_list:
    print(ts)
