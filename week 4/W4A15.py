"""
    x1+x2 = a
    2*x1 + 4*x2 = b
"""
a, b = map(int,input().split())
x2 = (b-2*a)/2
x1 = a-x2
if x1 != int(x1) : 
    print("invalid")
else : 
    print(int(x1),int(x2),sep = " ")