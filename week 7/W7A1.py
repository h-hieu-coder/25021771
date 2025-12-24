def binary_search(arr, val) : 
    n = len(arr) 
    left = 0 
    right = len(arr) - 1
    while left <= right : 
        mid = (left + right) // 2 
        if arr[mid] == val : 
            return mid 
        elif arr[mid] < val : 
            left = mid + 1
        else : 
            right = mid - 1
    return -1 

arr = list(map(int, input().split()))
val = int(input())
print(binary_search(arr,val))
