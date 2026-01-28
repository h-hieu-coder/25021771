#W9A5
a = list(map(int,input().split()))
b = list(map(int,input().split()))
n = len(a)
check = False
if n <= len(b):
    res = []
    for i in range(len(b)):
        if a[0] == b[i]:
            res.append(i)
    for x in res:
        if b[x:x+n] == a:
            check = True
            break
    if check :
        print("YES")
    else:
        print('NO')
else:
    print('NO')