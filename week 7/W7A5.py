arr = list(map(int, input().split()))
X = int(input())
n = len(arr) 
count = 0
for i in range(0,n) : 
    for j in range(i+1, n) :
        if arr[i] + arr[j] == X : 
            count += 1
print(count) 