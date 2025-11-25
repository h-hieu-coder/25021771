import sys 
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n = int(input())
max = n 
min = n
while n != -1 :
    n = int(input())
    if n > max : 
        max = n
    if n < min :
        min = n 
print(max, min ,sep = " ")