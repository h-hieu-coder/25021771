lst = list(map(str, input().split()))
n = len(lst) 
for i in range(n) : 
    try : 
        lst[i] = int(lst[i])
        print(lst[i])
    except : 
        print("Khong the chuyen phan tu thu",i,"sang kieu int")
