def Selection_Sort(arr) : 
    n = len(arr) 
    for i in range(0,n-1) : 
        min_index = i 
        for j in range(i+1,n): 
            if arr[j] < arr[min_index] : 
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] ,arr[i]
arr = list(map(int,input().split()))
Selection_Sort(arr) 
print(arr)