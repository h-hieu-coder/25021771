from math import sqrt 
x = int(input())
try : 
    res = '%.2f' % sqrt(x) 
    print(res)
except ValueError : 
    print("du lieu khong hop le")