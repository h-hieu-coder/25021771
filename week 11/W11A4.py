try : 
    a, b = map(int ,input().split())
    tong = a + b
except : 
    print("vui long nhap dung du lieu") 
else : 
    print(tong) 
finally : 
    print("Ket thuc chuong chinh.")