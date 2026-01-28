def reverse(path : str)-> int:
   with open(path , 'r') as f:
        ans = f.read()
   return ans[::-1]
path = input()
ans = reverse(path)
print(ans)
