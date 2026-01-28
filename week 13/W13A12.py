from itertools import islice
def MaximumProduct(path:str)->int:
   num = []
   with open(path , 'r') as f:
      n = int(f.readline().strip())
      lines = list(islice(f , n))
      for line in lines:
         num.append(int(line))
   num.sort(reverse=True)
   return num[0]*num[1]*num[2]    
path = input()
print(MaximumProduct(path))