def solve(path1 , path2): 
   s1 = ''
   s2 = ''
   with open(path1 , 'r') as f:
      s1 = list(f.read().strip())
   with open(path2 , 'r') as f:
      s2 = list(f.read().strip())
   map1 = {}
   map2 = {}
   for i in range(0 , len(s1)):
      if not s1[i].isalnum():
         continue
      s1[i] = s1[i].lower()
      if s1[i] not in map1:
         map1[s1[i]] = 1
      else:
         map1[s1[i]] += 1
   for i in range(0 , len(s2)):
      if not s2[i].isalnum():
         continue
      s2[i] = s2[i].lower()
      if s2[i] not in map2:
         map2[s2[i]] = 1
      else:
         map2[s2[i]] += 1
   for key in map1:
      if key not in map2:
         return False
      elif (map1[key] != map2[key]):
         return False
   for key in map2:
      if key not in map1:
         return False
   return True
path1 = input()
path2 = input()
print(solve(path1 ,path2))