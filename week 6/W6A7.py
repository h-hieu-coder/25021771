tup = tuple(map(str,input().split()))
print(tup[0],tup[-1], sep =" ", end = " ")
tup = tup[:: -1]
print(tup)