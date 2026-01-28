def reverse(path : str)-> bool:
   numrock = 0
   f = [False , True , True , True]
   with open(path , 'r') as v:
      numrock = int(v.read())
   i = 3
   while (i < numrock):
      i += 1
      if (f[i-1] and f[i-2] and f[i-3]):
         f.append(False)
      else:
         f.append(True)
   return f[numrock]   
path = input()
print(reverse(path))
