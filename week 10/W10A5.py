def solve(a, b) : 
    if not a : 
        return True 
    if not b : 
        return False 
    
    index_first = b.index(a[0])
    if index_first == -1 : 
        return False 
    
    return solve(a[1:], a[index_first +1 :])

a = [1, 2, 3, 4]
b = [2, 3, 1, 2, 3 , 4, 5 , 6]

if solve(a,b) : 
    print("YES")
else : 
    print("NO")