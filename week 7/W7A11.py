s = input()
a = input()
count = 0
while s.find(a) != -1 : 
  pos = s.find(a) 
  s = s[:pos] + s[pos + len(a):]
  count += 1
print(count)