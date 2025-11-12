""" day collatz :
        neu n chan , chia n cho 2
        neu n le , nhan n voi 3 roi cong 1
        lap lai quy tac den khi n bang 1
"""
def Collatz(n) :
    L = 0 
    while n != 1 : 
        L += 1
        if n%2 == 0 : 
            n//=2
        else :
            n = n*3 + 1
    return L+1

n = int(input())
L_max = 0
x_min = 1
for i in range(1,n+1):
    if L_max < Collatz(i) :
        L_max = Collatz(i)
        x_min = i 
print(x_min,L_max,sep=" ")