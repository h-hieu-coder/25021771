# tim ucln sau do tim uoc cua ucln 
def ucln(a,b):
    while b != 0 :
        a, b = b, a%b
    return a
a,b = map(int, input().split())
GCD = ucln(a,b)
for i in range(1,GCD+1):
    if GCD%i == 0 : 
        print(i,end = " ")