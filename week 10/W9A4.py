#W9A4
t = int(input())
for _ in range(t):
    a = input()
    lst_a = list(a)
    b = input()
    check = True
    tmp = list(a)
    for ch in lst_a:
        if ch.upper() not in b:
            tmp.remove(ch)
    if len(tmp) != len(b):
        check = False
    else:
        a = "".join(tmp)
        if a.upper() != b:
          check = False
    if check:
        print('YES')
    else:
        print('NO')