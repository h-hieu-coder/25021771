# Bai 5 : nhap chu cai in hoa A , xuat ra chu cai thuong lien truoc a tuong ung cua A
s = input()
if (s == "A") :
    print("khong ton tai")
else :
    s = s.lower()
    s = ord(s)-1
    print(chr(s))