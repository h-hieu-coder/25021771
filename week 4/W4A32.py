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
if hoa >= 1 and thuong >= 1 and so >= 1 : 
    print("YES")
else : 
    print("NO")