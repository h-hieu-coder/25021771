n,m = map(int, input().split())
a = []

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(int(input()))

print(a)
print(a[1][0])