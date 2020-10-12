#Bài tập 01:Viết chương trình nhập xuất mảng 1 chiều (List).
#a. Tính tổng của mảng 1 chiều.
print("Bài 1: ")
print("a. Tính tổng của mảng 1 chiều. ")
t=int(input("nhap t= "))
def tong(t):
    tong = 0
    arr = []
    for i in range (t):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
        tong+=arr[i]
    return tong
print(tong(t))        

#b. Tính tích mảng 1 chiều.
print("b. Tính tích mảng 1 chiều. ")
t =int(input("nhap t= "))
def tich(t):
    tich = 1
    arr = [] 
    for i in range (t):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
        tich*=arr[i]
    return tich
print(tich(t))

#c. Tìm giá trị lớn nhất.
print("c. Tìm giá trị lớn nhất. ")
t =int(input("nhap t= "))
def max(t):
    arr =[]
    for i in range (t):
        x = input(f"input item[{i}]:")
        arr.append(int(x))
    max = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] > max):
            max=arr[i]
    return max
print(max(t))                

#d. Tìm giá trị nhỏ nhất.
print("d. Tìm giá trị nhỏ nhất. ")
t =int(input("nhap t= "))
def min(t):
    arr =[]
    for i in range (t):
        x = input(f"input item[{i}]:")
        arr.append(int(x))
    min = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] < min):
            min=arr[i]
    return min
print(min(t))

#e. Tìm các số lẻ trong mảng.
print("e. Tìm các số lẻ trong mảng. ")
t =int(input("nhap t= "))
def sole(t):
    result = []
    arr = []
    
    for i in range (t):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    for i in range(0,len(arr)):
        if ( arr[i] % 2 != 0 ):
            result.append(arr[i])
    return result
print("cac so le trong mang la: ",sole(t))

#f. Tìm các số chẵn trong mảng.
print("f. Tìm các số chẵn trong mảng. ")
t=int(input("nhap t= "))
def sochan(t):
    result = []
    arr = []
    
    for i in range (t):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    for i in range(0,len(arr)):
        if ( arr[i] % 2 == 0 ):
            result.append(arr[i])
    return result
print("cac so chan trong mang la: ",sochan(t))

#Bài tập 02:
print("Bài tập 02: ")
t =int(input("nhap t= "))
def timidbaihat(t):
    result =[]
    arr = []
    count =0
    
    for i in range (t):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    for i in arr:
        if i not in result:
            result.append(i)
            count+=1
    return count,result
print(timidbaihat(t))

#Bài tập trên zalo:
#Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
print("Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ. ")
list1=[1,10,00]
arr= []
t = int(input("nhap t= "))
for i in range (t):
    x = input(f"input item[{i}]: ")
    arr.append(int(x))
print(arr)
print(list1)
print(list1 + arr)




