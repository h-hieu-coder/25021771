def BinarySearch(arr,Val) : 
    left = 0 
    right = len(arr) - 1
    while left <= right : 
        mid = (left + right) // 2

        if arr[mid] == Val : 
            return mid 
        
        if arr[mid] < Val : 
            left = mid + 1
        else : 
            right = mid - 1
    return -1 

arr = list(map(int,input().split()))
Val = int(input())
print(BinarySearch(arr,Val))