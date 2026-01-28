import csv 
def findMovies(file):
   with open(file ,'r') as f:
      reader = csv.DictReader(f)
      for row in reader:
         if (row['description'] != 'boring') and (float(row['rating']) >= 8.0):
            print(row['movie'])
filename = input()
findMovies(filename)