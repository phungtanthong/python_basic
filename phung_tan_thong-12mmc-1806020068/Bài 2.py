# Đề 1:
# Bài 2:
print("Bài 2: ")
def mua(t):
    if ( t == 1 or t <= 3):
        return("Xuân")
    elif (t == 4 or t <= 6):
        return("Hạ")
    elif ( t == 7 or t <= 9):
        return("thu")
    elif ( t == 10 or t <=12):
        return("đông")
    else:
        return("nhap sai thang trong nam")
if __name__ == "__main__":
    t=int(input("nhap t= "))
    print(mua(t))