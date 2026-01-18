def merge(a,b) : 
    if not a : 
        return b 
    if not b : 
        return a 
    
    if a[0] <= b[0] : 
        return [a[0]] + merge(a[1:] ,b)
    else : 
        return [b[0]] + merge(a, b[1:])
    
arr = []
n = 0
k = None
while True : 
    try : 
        arr1 = list(map(int, input().split()))
        if len(arr1) == 1 : 
            k = arr1[0]
            break 
        n += 1
        arr = merge(arr,arr1)

    except EOFError: 
        break

print(arr[k])