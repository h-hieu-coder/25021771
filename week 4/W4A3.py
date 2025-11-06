def Giai_thua(n) : 
    res = 1
    while n>0 : 
        res *= n 
        n -= 1
    return res
n = int(input())
print(Giai_thua(n))