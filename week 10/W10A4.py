def solve(a, b):
    if b == "":
        return True
    if a == "":
        return False

    index_first = a.find(b[0])
    if index_first == -1:
        return False
    
    return solve(a[index_first + 1:], b[1:])

n = int(input())
while n > 0 : 
    n -= 1
    a = input()
    b = input()

    a = a.lower()
    b = b.lower()

    if solve(a, b):
        print("YES")
    else:
        print("NO")
