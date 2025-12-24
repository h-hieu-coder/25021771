def LenearSearch(arr,Val) : 
    j = 0 
    for i in arr :
        if i == Val :
            return j
        j += 1
    return -1 
arr = list(map(int, input().split()))
Val = int(input())
print(LenearSearch(arr,Val))