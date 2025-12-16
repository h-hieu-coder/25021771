list = list(map(int,input().split()))
k = int(input())
for i in range(0,k) :
    list.append(list[0]) 
    list.remove(list[0]) 
tup = tuple(list)
print(tup)