print("Bai 4: "0)
a=int(input("nhap a= "))
b=int(input("nhap b= "))
c=int(input("nhap c= "))
if( (a<b+c)&(b<a+c)&(c<a+b) ):
    if( (a*a==b*b+c*c) | (b*b==a*a+c*c) | (c*c== a*a+b*b)):
        print("đây là hình tam giác vuông")
    else:
       print("đây là hình tam giác nhưng không phải là hình tam giác vuông")
else:
    print("đây không phải hình tam giác")