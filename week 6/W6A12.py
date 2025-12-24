arr = list(map(int, input().split()))

cnt = {}
max_val = 0
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

    if max_val < cnt[i] : 
        max_val = cnt[i]

arr.sort() 
for i in arr : 
    if cnt[i] == max_val : 
        print(i) 
        break 