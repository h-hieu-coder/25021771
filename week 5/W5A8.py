a, b = map(int,input().split())
def hamming(a,b):
    xor = a^b
    num = int(str(bin(xor)[2:]))
    res = 0 
    while num > 0 : 
        if num%10 == 1 : 
            res += 1
        num //= 10 
    return res 
print(hamming(a,b))