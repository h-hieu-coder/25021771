try : 
    a = int(input())
    arr = set()
    while a != 1 : 
        if a in arr : 
              print("NO") 
              break 
        arr.add(a) 

        res = 0 
        for i in str(a) : 
            res += int(i) ** 2
        a = res 
    if a == 1 : 
        print("YES") 

except ValueError :  
    print("Loi nhap lieu")