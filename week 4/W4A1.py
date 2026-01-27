def  Sum(n):
    sum = 0 
    while n>0 :
        sum +=n 
        n -= 1
    return sum 
n = int(input())
print(Sum(n))#