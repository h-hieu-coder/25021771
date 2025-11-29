n = int(input())
def giai_thua(n) : 
    res = 1
    while n > 0 : 
        res *= n 
        n -= 1
    return res 
print(giai_thua(n))