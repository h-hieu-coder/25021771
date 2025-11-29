n = int(input())
def tong_chu_so(n) : 
    res = 0 
    while n > 0 :
        res += n%10 
        n //= 10
    return res 
print(tong_chu_so(n))