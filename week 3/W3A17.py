a,b,c = map(int,input().split())
if (a+b) <= c or (b+c) <= a or (c+a) <= b : 
    print("Khong phai tam giac") 
elif a == b == c : 
    print("Tam giac deu")
elif a == b or b == c or c == a : 
    print("tam giac can") 
else : 
    print("Tam giac thuong")