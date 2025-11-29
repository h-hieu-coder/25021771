len = input()
hoa = 0 
thuong = 0
so = 0
for i in len : 
    if "A" <= i and i <= "Z": 
        hoa += 1 
    if "a" <= i and i <= "z":
        thuong += 1 
    if "1" <= i and i <= "9" :
        so += 1
print(hoa , thuong , so , sep = " ")