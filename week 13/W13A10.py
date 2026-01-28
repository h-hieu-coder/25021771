def getMoney(path:str):
   ans = []
   with open(path , 'r') as f:
      ans = f.read().split()
   ans = [int(x) for x in ans]
   return ans
def rob(a):
   f = [0]*len(a)
   f[0] = a[0]
   f[1] = a[0]
   for i in range(2 , len(a)):
      f[i] = max(f[i-1] , f[i-2] + a[i])
   return f[len(f) - 1]
path = input()
Money = getMoney(path)
print(rob(Money))