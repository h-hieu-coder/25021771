money , month = map(int, input().split())
r = 0.7/100 
print(int(money*(1+r)**month))