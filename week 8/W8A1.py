pi = 3.14
def S_tp(R, h) : 
    S_tp = 2*pi*R*h + pi*R*R
    print('%.2f'%S_tp , end = " ")

def V(R,h) : 
    V = pi*R*R*h
    print('%.2f'%V)

R, h = map(float, input().split())

S_tp(R, h)
V(R, h)