list = list(map(int,input().split()))
map = {"positives" : 0 , "negatives" : 0 , "zero" : 0}
for i in list : 
    if i < 0 : 
        map["positives"] += 1
    elif i > 0 : 
        map["negatives"] += 1
    else : 
        map["zero"] += 1
print(map)