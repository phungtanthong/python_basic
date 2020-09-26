#1. Xuất ra màn hình N lần câu thông báo "Hello python"
n= int(input('nhap n=' ))
for n in range (0,n,1):
    print("Hello Python")


#2. Tính tổng từ 1 cho đến N
n= int(input('nhap n= '))
sum = 0
for i in range (1,n+1):
    sum += i
print("Tong tu 1 den", n ,"la: ", sum )


#3. Tính tổng các số chẵn nằm trong đoạn từ 0 đến N
n= int(input('nhap n='))
chan=0
for i in range (0,n+1):
    if(i % 2 == 0):
        chan += i
        print (i)
    else:
        print(0)
print("tong cac so chan",chan)        


#4. Tính tổng các số LẼ nằm trong đoạn từ 0 đến N
n= int(input('nhap n='))
le=0
for i in range (0,n+1):
    if(i % 2 !=0 ):
        le +=i
        print (i)
    else:
        print ()
print("tong cac so le",le)        


#5.	Tính trung bình cộng các số trong mảng
n = int(input('nhap n= '))
tong=0
i=1
tongtrungbinh = int
for i in range(i,n+1):
    tong +=i
    print (tong)
tongtrungbinh = tong / n
print("tong trung binh cong trong mang ", tongtrungbinh)

#6.	Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
n = int(input('nhap n= '))
tong = 0
for i in range (1,n+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print (tong)

#7.	Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua
n= int(input('nhap n= '))
tong= 0
for i in range (1,n+1):
    if(i == 17):
        continue
         
    else:
        tong += i
        print(i, tong)
print (tong)

