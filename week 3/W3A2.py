a, b = map(int, input().split())
a = a^b
b = a^b # b = (a^b)^b = a
a = a^b # a = (a^b)^a = b
print(a,b,sep =" ")