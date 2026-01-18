lst = list(map(int, input().split()))
arr1 = [] 
arr2 = []
for i in lst : 
    if i % 2 == 0 : 
        arr1.append(i) 
    else : 
        arr2.append(i)
print(tuple(arr1), tuple(arr2) , sep = "\n")