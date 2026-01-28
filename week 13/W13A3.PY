from itertools import islice 
def HouseOfhogwart(path: str):
    ans = []
    with open(path , 'r' , encoding='utf-8') as f:
      n = int(f.readline().strip())
      lines = islice(f , n)
      for line in lines:
         print(line.strip())
path = input()
HouseOfhogwart(path)