from math import sqrt
n = int(input())
can = int(sqrt(n))
res = 0 
for i in range(1,can+1) : 
    if n%i == 0 :
        if i%2 == 0 :
            res += 1
        if i!=(n//i) and (n//i)%2 == 0 :
            res += 1
print(res)