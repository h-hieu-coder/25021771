def dist(x , y):
   return float((x**2 + y**2)**0.5)
def estimated(path :str):
   with open(path ,'r') as f:
      a = f.read().split()
      st = [float(a[2]) , float(a[4])]
      en = [float(a[7]) , float(a[9])]
      v = float(a[11])
      return float(dist(en[0] - st[0] , en[1] - st[1])/v)
path = input()
print(f'{estimated(path):.2f}')