print("Bai 2: ")
s=1
x=int(input("nhap x= "))
n=int(input("nhap n= "))
for i in range (1,n+1):
    s1= s  + pow(x,i)
print("kết quả của S1 là: ", s1  )
for i in range (0,n+1):
    s2=s + ((-1)* pow(x,i) )
print("kết quả của S2 là: ",s2)