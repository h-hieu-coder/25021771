len = input()
k = input()
def vi_tri(len,k) : 
    num = len.split()
    j = 0
    for i in num : 
        j += 1
        if i == k : 
            break 
    return j
print(vi_tri(len,k))
       