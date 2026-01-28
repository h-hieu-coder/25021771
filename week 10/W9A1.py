#W9A1
def merge_recursive(a,b):
  if not a:
    return b
  if not b:
    return a
  res = []
  if a[0]>b[0]:
    res = [b[0]] + merge_recursive(a,b[1:])
  else:
    res = [a[0]] + merge_recursive(a[1:],b)
  return res
a= list(map(int,input().split()))
b= list(map(int,input().split()))
print(*merge_recursive(a,b))