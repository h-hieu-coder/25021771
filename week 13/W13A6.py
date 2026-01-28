def count(path : str , char : str):
   s = ''
   with open(path , 'r') as f:
      s = f.read().split()
   cnt = 0
   for i in range(0 , len(s)):
      s[i] = s[i].lower()
      for word in s[i]:
         if (word == char):
            cnt += 1
   return cnt 
path = input()
char = input()
print(count(path , char))