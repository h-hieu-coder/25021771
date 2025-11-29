from math import sqrt 
def kt_nto(n) : 
    if n<=0 : 
        return False 
    dem = 0
    can = int(sqrt(n))
    for i in range(1,can+1):
        if n%i == 0 :
            dem += 1
    if dem == 1 : 
        return True 
    else :
        return False 
