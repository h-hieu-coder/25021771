dict1 = eval(input())
dict2 = eval(input())

for key in dict2.keys() : 
    if key in dict1 : 
        dict1[key] += dict2[key]
    else : 
        dict1[key] = dict2[key] 
    
dict1 = dict(sorted(dict1.items()))
print(dict1)

