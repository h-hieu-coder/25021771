n = int(input())
chan = 0
le = 0
while n>0 : 
    so = n%10 
    if so%2 == 0 : 
        chan += 1 
    else : 
        le += 1
    n //= 10
print(chan ,le ,sep = " ")