lst = list(map(int, input().split()))
k = int(input())
while k > 0 : 
    lst.append(lst[0])
    lst = lst[1:]
    k -= 1

print(tuple(lst))