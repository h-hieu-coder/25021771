def count_occurrences(arr, x) : 
    n = len(arr) 
    count = 0 
    for i in range(0,n) : 
        if arr[i] == x : 
            count += 1
    return count 

arr = list(map(int, input().split()))
val = int(input())
print(count_occurrences(arr, val))