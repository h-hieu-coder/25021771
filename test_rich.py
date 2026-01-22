def solve(a,b) : 
    dicta = {} 
    dictb = {}

    for i,j in zip(a,b) : 
        if i not in dicta : 
            dicta[i] = j 
        else : 
            if dicta[i] != j : 
                return False  
        
        if j not in dictb : 
            dictb[j] = i 
        else :
            if dictb[j] != i  :
                 return False 
    return True 
a, b = map(str, input().split())
 
if solve(a,b) : 
    print("true") 
else : 
    print("false")