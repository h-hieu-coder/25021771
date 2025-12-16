list = list(map(str,input().split()))
mp = {}
for i in list  : 
    if i in mp : 
        mp[i] += 1
    else : 
        mp[i] = 1
print(mp)