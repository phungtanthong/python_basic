#Bài 1: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
print("Bài 1: ")
chuoi=input("nhap chuoi:")
def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]
print(manual_replace(chuoi,"$", 0))

#Bài 2: Viết chương trình để xoá bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
print("Bài 2: ")
chuoi=input("nhap chuoi:")
def remove_char_m(str, n):
      phan_dau=str[:n] 
      phan_cuoi=str[n+1:]
      return phan_dau + phan_cuoi
print(remove_char_m(chuoi,int(input("thu tu muon xoa:"))))

#Bài 3: Viết chương trình để xoá bỏ các ký tự có số là số lẻ trong một chuỗi.
print("Bài 3: ")
chuoi = input("nhap chuoi:")
def even_values_string(str):
  ketqua = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      ketqua = ketqua + str[i]
  return ketqua
print(even_values_string(chuoi))

#Bài 4: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
print("Bài 4: ")
chuoi = input("nhap chuoi:")
def dau_va_duoi(str):
  if len(str) < 2:
    return "chuoi rong"
  return str[0:2] + str[-2:]
print(dau_va_duoi(chuoi))

#Bài 5: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím.
print("Bài 5: ")
chuoi = input("nhap chuoi:")
print("ki tu lon nhat cua chuoi:", max(chuoi))
print("ki tu nho nhat cua chuoi:", min(chuoi))

#Bài 6: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong mỗi chuỗi.
print("Bài 6: ")
chuoi = input("nhap chuoi:")
print(chuoi.swapcase())

