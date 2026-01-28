import csv
def averageTime(path:str):
   sum = 0.0
   cnt = 0
   with open(path , 'r') as f:
      reader = csv.DictReader(f)
      for row in reader:
         sum += float(row['Time'])
         cnt += 1
   return f'{sum / cnt :.2f}'
path = input()
print(averageTime(path))