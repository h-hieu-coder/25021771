s = input()
s = s.replace('[', '').replace(']', '').replace(',' ,'')

lst = list(map(int, s.split()))
print(lst)