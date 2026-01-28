import csv 
path = input()
with open(path , 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if (row['THCS4'] == '10'):
            print(row['Ho'] ,row['Ten'])