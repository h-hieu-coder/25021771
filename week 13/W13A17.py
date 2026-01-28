def ProductExceptSelf(path:str) -> list:
   ans = []
   with open(path , 'r') as f:
      origin = f.read().split()
      origin = [int(origin[x]) for x in range(1 , len(origin))]
      product = 1
      for i in range(0 , len(origin)):
         product *=origin[i]
      for i in range(0 , len(origin)):
         print(product//origin[i] , end=' ')
path = input()
ProductExceptSelf(path)