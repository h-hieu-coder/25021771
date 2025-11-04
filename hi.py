from math import sqrt
import sys 
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
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
n = int(input())
if kt_nto(n) :
    print("n la so nguyen to")
else :
    print("n khong la so nguyen to")

