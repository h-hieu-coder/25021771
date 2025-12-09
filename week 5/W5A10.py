def ktra(a,b) :
    map_a_to_b = {} 
    map_b_to_a = {}

    for c1,c2 in zip(a,b) : #duyệt đồng thời các ký tự cùng thứ tự trên a và b
        
        if c1 in map_a_to_b : 
            if map_a_to_b[c1] != c2 : 
                return False 
        
        if c2 in map_b_to_a :
            if map_b_to_a[c2] != c1 :
                return False
        
        map_a_to_b[c1] = c2 
        map_b_to_a[c2] = c1
    
    return True

a,b = map(str, input().split())

if ktra(a,b) : print("true")
else : print("false")