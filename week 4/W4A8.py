# ham dao nguoc 
def reverse(n):
    res = 0
    while n>0 : 
        res =  res*10 + n%10
        n //= 10 
    return res 
# ham kiem tra doi xung  
def doi_xung(n):
    return n == reverse(n)

n = int(input())
dem = 0
while doi_xung(n) == False :
    n += reverse(n)
    dem += 1
print(dem,n,sep = " ")