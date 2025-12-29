n = int(input()) 
lst = [] 
m = 0 
index_Nemo = None
while m < n : 
    name = input()
    lst.append(name) 
    if name == "Nemo " : 
        index_Nemo = m
    m += 1

if index_Nemo == 0 : 
    print(lst[n-1],"and ",lst[1], sep = "") 
elif index_Nemo == n-1 : 
    print(lst[n-2],"and ",lst[0],sep = "")
else : 
    print(lst[index_Nemo-1],"and ",lst[index_Nemo+1], sep = "") 