l1 = list(map(int, input().split()))
try : 
    l2 = list(map(int,input().split()))
except : 
    print("[]")

lst = [] 
for x in l1 : 
    if x in l2 and x not in lst : 
        lst.append(x) 
print(lst)