# Đề 1:
# Bài 4:
print("Bài 4: ")
print("Bài 4: ")
def Tiencuocdienthoai(t):
    
    p = t.split(";")
    tg = p[1].split(":")
    tong_so_phut = float(tg[0]) * 60 + float(tg[1]) + float(tg[2]) / 60
    money = tong_so_phut * 2500
    return int(money)
if __name__ == "__main__":
    t=str(input("nhap vao mot chuoi bat ki: "))
    print("tính giá cước trên là: ",Tiencuocdienthoai(t))