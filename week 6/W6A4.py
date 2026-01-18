s = input().split()
dct = {}
for pair in s: 
    key, value = pair.split(":")

    if key not in dct : 
        dct[key] = [value] 
    else : 
        dct[key].append(value) 

print(dct) 