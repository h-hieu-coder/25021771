#W9A2
def findk(a):
  res = []
  if not a:
    return []
  else:
    min_val = min(a)
    a.remove(min(a))
    res = [min_val] + findk(a)
  return res
a = []
n = int(input())
for i in range(n):
  a.extend(list(map(int,input().split())))
k = int(input())
res = findk(a)
print(res[k-1])