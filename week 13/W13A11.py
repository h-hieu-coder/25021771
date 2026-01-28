import os
def solve(filepath):
   if os.path.exists(filepath) and os.path.isfile(filepath):
      with open(filepath , 'r') as f:
         num = f.read().split()
      if not num:
         return "Mission failed"
      num = [int(x) for x in num]
      minn = 1e9 
      maxn = -1e9
      for i in range(0 , len(num)):
         minn = min(minn , num[i])
         maxn = max(maxn , num[i])
      return f'{maxn} {minn}'
   else:
      return "Mission failed"
filepath = input()
print(solve(filepath))