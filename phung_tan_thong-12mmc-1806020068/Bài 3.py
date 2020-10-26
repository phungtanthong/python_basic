# Đề 1:
#Bài 3:
print("Bài 3: ")
def tinh_tong(t):
    tong = 0
    for i in range (0,t):
        if (i == 13 ):
            break
        else:
            tong += i
        
    return tong
if __name__ == "__main__":
    t=int(input("nhap t= "))
    print("Tổng các giá tri từ 1 đến ",t," là: ",tinh_tong(t))