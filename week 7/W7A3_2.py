def Selection_Sort(arr) : 
    n = len(arr)
    for i in range(0,n-1) : 
        min_index = i 
        for j in range(i+1 , n) : 
            if arr[min_index] > arr[j] :
                min_index = j 
        arr[min_index] ,arr[i] = arr[i], arr[min_index] 

arr = list(map(int, input().split()))
Selection_Sort(arr)
for i in arr :
    print(i, end = " ")