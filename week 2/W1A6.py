# Bai 6 Kiem tra va tinh dien tich tam giac
from math import sqrt
a,b,c = map(int, input().split())
if(a+b<=c or b+c<=a or a+c<=b) :
    print("Khong phai tam giac")
else :
    p = (a+b+c)/2
    s_binh = p*(p-a)*(p-b)*(p-c)
    s = sqrt(s_binh)
    print(round(s,1))