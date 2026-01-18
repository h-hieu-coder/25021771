def merge(a, b):
    # Điều kiện dừng
    if not a:
        return b
    if not b:
        return a
    
    # Bước đệ quy
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr = merge(arr1, arr2)
for i in arr : 
    print(i, end = " ")