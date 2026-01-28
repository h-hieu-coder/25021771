def count(path : str , char : str):
   s = ''
   with open(path , 'r') as f:
      s = f.read().strip()
   cnt = 0
   for i in range(0 , len(s)):
      if (s[i] == char):
         cnt += 1
   return cnt 
path = input()
char = input()
print(count(path , char))