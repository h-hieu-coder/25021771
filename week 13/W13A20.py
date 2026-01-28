def solve(path):
    a = []
    with open(path , 'r') as f:
         dx = [0 , 0 ,1 , - 1 , 1 , - 1 , 1 , -1]
         dy = [-1 , 1 ,1 , - 1, 0 , 0 , -1 , 1]
         for line in f:
            row = [int(x) for x in line.split()]
            if row:
                a.append(row)
         for i in range(0 , len(a)):
            for j in range(0 , len(a[i])):
               sum = a[i][j]
               cnt = 1
               for k in range(0 , 8):
                   ndx = dx[k] + i
                   ndy = dy[k] + j
                   if ((ndx<len(a)) and (ndx >=0)) and ((ndy < len(a[i])) and (ndy >=0)):
                       sum += a[ndx][ndy]
                       cnt += 1
               a[i][j] = sum // cnt
    return a
path = input()
ans = solve(path)
for i in range(0 , len(ans)):
   for j in range(0 , len(ans[i])):
       print(ans[i][j],end = ' ')
   print()