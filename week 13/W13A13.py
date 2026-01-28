from itertools import islice
def moveZeroes(filename:str)-> list:
   origin = []
   ans = []
   with open(filename, 'r') as f:
      n = int(f.readline().strip())
      nums = list(islice(f , n))
      for num in nums:
         origin.append(int(num))
   ans = [x for x in origin if (x != 0)]
   while (len(ans) != len(origin)):
      ans.append(0)
   return ans
filename = input()
print(moveZeroes(filename))