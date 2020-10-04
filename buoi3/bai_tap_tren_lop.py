#Bài 1: Tìm số đảo của số n
print("Bài 1: ")
n = int(input("nhap n= "))
def daonguoc(n):
    return(str(n)[::-1])
print(daonguoc(n))

#Bài 2: Tính n!
print("Bài 2: ")
n = int(input("nhap n= "))
def tinhgiaithua(n):
    if n == 0:
        return 1
    return n * tinhgiaithua(n - 1)
print("Giai thua của ",n," là ",tinhgiaithua(n))

#Bài 3: Tính tổng 1^3+2^3+n..n^3
print("Bài 3: ")
n = int(input("nhap n= "))
s=0
for i in range (1,n+1):
    s= s + pow(i,3)
    print(s)

#Bài 4: tính tổng các số lẻ
print("Bài 4: ")
n = int(input("nhap n = "))
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 != 0):
            s+=i
    print(f"tong cac so le la: ", s)
    return s
print(tong(n))

#Bài 5: Tính tổng các chữ số chẳn
print("Bài 5: ")
n = int(input("nhap n = "))
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 == 0):
            s+=i
    print(f"tong cac so chan la: ", s)
    return s
print(tong(n))

#Bài 6: Xem 1 số có phải là số nguyên tố hay không 
print("Bài 6: ")
def songuyento(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "là số nguyên tố"
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print(songuyento(n))

#Bài 7: Xem 1 số có phải là số chính phương hay không
print("Bài 7: ")
import math
n=int(input("nhap n= "))
x = math.sqrt(n)
def sochingphuong(n):
    if(x * x == n):
        return "là số chính phương"
    else:
        return  "không phải là số chính phương"
print(n,sochingphuong(n))

#Bài 8: Tính tổng các số nguyên tố 1 đến n
print("Bài 8: ")
def songuyento(n):
    count = 0
    s =0 
    for i in range(1, n + 1):
        if n % i == 0:
            s=s+i
            count += 1
    if count == 2:
        return s
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print("tong cac so nguyen to la: ",songuyento(n))

#Bài 9: In ra bảng cửu chương n
print("Bài 9: ")
n= int(input("nhap n= "))
def bangcuuchuong(n):

    for j in range(1,10):
        s = n * j
        print(n, "*" ,j, "=" ,s)
    return s
print(bangcuuchuong(n))

#Bài 10: Tính số fibo thứ n
print("Bài 10: ")
def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input("nhap n = "))
print(fibonacci(n))
