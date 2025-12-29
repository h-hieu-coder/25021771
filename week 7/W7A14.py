n = int(input())
arr = list(map(int, input().split()))
res = False 
for i in range(n-1, -1, -1) :
    if arr[i] == 7 : 
        print(i,end = " ")
        res = True
if res == False : 
    print("Not found")