from math import sqrt 
# ham kiem tra xem so nguyen co cac chux so doi mot khac nhau khong
def kiem_tra_lap(n):
    arr = []
    for i in range(0,10) :
        arr.append(0)
    while n>0 : 
        arr[n%10] += 1
        n //= 10
    res = True
    for i in arr :
        if i>1 :
            res = False 
            break
    return res

n = int(input())
can = int(sqrt(n))
for i in range(1,can+1):
    if kiem_tra_lap(i*i) :
        print(i*i,end = " ")