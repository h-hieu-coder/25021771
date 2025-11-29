from math import sqrt 
def hoan_hao(n):
    can = int(sqrt(n))
    sum = 0
    if can*can == n :
        sum += can
        for i in range(1,can) :
            if n%i == 0 :
                sum = sum + i + n//i
    else : 
        for i in range(1,can+1) :
            if n%i == 0 : 
                sum = sum + i + n//i
    return sum == 2*n