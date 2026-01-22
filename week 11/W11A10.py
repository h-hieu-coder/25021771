def check(lst) : 
    arr = [] 
    for i in lst : 
        if i in arr : 
            return False 
        else : 
            arr.append(i)
    return True
lst = list(map(int, input().split()))
n = lst[0]
lst = lst[1:]

try : 
    if check(lst) : 
        res = 0 
        for i in lst : 
            res += i 
        print(res)
    else :
        raise ValueError
except ValueError : 
    print("Mang khong hop le")