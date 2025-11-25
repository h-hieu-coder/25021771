"""Thuat toan Euclid :
 UCLN(a,b) = UCLN(b,a%b)
 lap lai den khi b = 0 thi ucln chinh la a
"""
def ucln(a,b):
    while b != 0 :
        a, b = b, a%b
    return a
m,n = map(int, input().split())
GCD = ucln(m,n)
print(GCD)