arr = list(map(int,input().split()))
k = int(input())

res = [] 

n = len(arr)
for i in range(0,n) : 
    for j in range(i+1,n) : 
        if arr[i] + arr[j] == k : 
            res.append((arr[i] , arr[j]))
            