def solve(arr) : 
    mp = {} 
    n = len(arr) 
    max_count = 0
    for i in range(0, n) : 
        if arr[i] in mp : 
            mp[arr[i]] += 1
        else : 
            mp[arr[i]] = 1

        if mp[arr[i]] > max_count : 
            max_count = mp[arr[i]] 

    for i in range(0,n) : 
        if mp[arr[i]] == max_count : 
            return arr[i] , max_count 
        
arr = list(map(int,input().split()))
val , max_count = solve(arr) 
print(val,"xuat hien nhieu nhat,som nhat,",max_count,"lan")