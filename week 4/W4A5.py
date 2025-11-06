n = int(input())
num = list(map(int,input().split()))
res = 0
for i in num:
    if i == 42: 
        print("I've found the meaning of life!")
        res = 1
        break 
if res == 0: 
    print("It′s a joke!")
