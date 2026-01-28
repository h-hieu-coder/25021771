n = int(input())
f = ['a' , 'b']
while (len(f) <= n):
   i = len(f) - 1
   f.append(f[i - 1] + f[i - 2])
with open("output.txt" , 'w') as v:
   for i in range(0 , n + 1):
      line = f"f({i})={f[i]}\n"
      v.write(line)  