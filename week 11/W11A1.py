a,b = map(int, input().split())

try : 
    if b != 0 : 
        res = '%.2f' % (a/b) 
        print(res) 
    else : 
        raise ValueError 
except ValueError : 
    print("Loi chia khong")